#!/usr/local/bin/python3
# coding=utf-8
from time import sleep
import config as c
import random
from crypto import *


def tFunction_proxy(proxy_to_server, server_to_proxy, stash_size, nodeList, proxy, block_list):
    '''
    The target function running by proxy.
    :param proxy_to_server: communication queue
    :param server_to_proxy: communication queue, end service when detect 0
    :param stash_size: current stash size
    :param nodeList:
    :param proxy:
    :return: None
    '''
    print('Start Proxy.')
    stash = []
    for _ in range(stash_size):
        stash.append([])
    stash_next_location = 0
    while True:
        share = 0
        for i in range(len(nodeList)):
            _share = server_to_proxy[i].get()
            share += _share
            print('Proxy: Read {1} from {0}'.format(i, _share))
            # sleep(1)

        if share == 0:
            print('End Proxy.')
            break

        share = share - len(nodeList)
        inStash = False
        for i in stash:
            if share == i:
                inStash = True
                break
        if inStash:
            share = len(block_list) - stash_size + proxy.queryCount
            query_result = proxy.query(share)   # oblivious operation
            query_result = block_list[i]
            print('stash')
        else:
            stash[stash_next_location] = share
            stash_next_location = (stash_next_location + 1) % stash_size
            query_result = proxy.query(share)

        print('Proxy Stash: {0}'.format(stash))
        print('Proxy Query Result: {0}'.format(query_result))
        query_result = aes_encrypt(query_result, c.k_new)
        en_result_share_list = c.generate_random_secret_share_block(query_result, len(nodeList))
        # query_result = aes_decrypt(query_result, c.k_new)

        for i in range(len(nodeList)):
            proxy_to_server[i].put(en_result_share_list[i])

        if proxy.queryCount == stash_size:
            print('Proxy: Shuffle.')
            proxy.shuffle()
        sleep(0)


def tFunction_server(proxy_to_server, server_to_proxy, server_to_client, client_to_server, nodeList, node):
    '''
    The target function running by servers.
    :param proxy_to_server: communication queue,
    :param server_to_proxy: communication queue, put 0 to end service
    :param server_to_client: communication queue
    :param client_to_server: communication queue, end service when detect 0
    :param nodeList:
    :param node:
    :return: None
    '''
    print('Start Server {0}.'.format(node.id))

    while True:
        resquest_share = client_to_server[node.id].get()
        if resquest_share == 0:
            server_to_proxy[node.id].put(0)
            print('End Server {0}.'.format(node.id))
            break
        node.put_request(resquest_share)
        print('{0}: Get {1}.'.format(node.id, node.request_share))

        server_to_proxy[node.id].put(node.request_share)
        print('{0}: Request Share Send End.'.format(node.id))

        sleep(0)
        en_result_share = proxy_to_server[node.id].get()
        server_to_client[node.id].put(en_result_share)


def tFunction_client(server_to_client, client_to_server, len_block_list, dummy_size, nodeList):
    '''
    The target function running by client.
    :param server_to_client: communication queue
    :param client_to_server: communication queue, put 0 to end service
    :param dummy_size:
    :param nodeList:
    :return: None
    '''
    print('Start Client.')
    for j in range(c.qNumber):
        share_list = c.generate_random_secret_share_index(random.randint(0, len_block_list - 1 - dummy_size) + len(nodeList),
                                                          len(nodeList))
        for i in range(len(nodeList)):
            client_to_server[i].put(share_list[i])

        de_result_block = ''
        for i in range(len(nodeList)):
            de_result_block += server_to_client[i].get()
        query_result = aes_decrypt(de_result_block, c.k_new)
        print('Client Query Result: {0}'.format(query_result))
        print('Client Query Round {0} End.'.format(j + 1))
        sleep(1)

    for i in range(len(nodeList)):
        client_to_server[i].put(0)
