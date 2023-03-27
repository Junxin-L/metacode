#!/usr/local/bin/python3
# coding=utf-8
import random
from multiprocessing import Process
from target import *
from nodes import *
from proxy import *
import config as c




def run(processList):
    '''
    Start all threads including one proxy, one client and N servers.
    To ensure synchronous startup, merging the operation of start and join is not allowed.
    :return: None
    '''
    for process in processList:
        process.start()
    for process in processList:
        process.join()



def init():
    '''
    Init the threads including one proxy, one client and N servers.
    :return: process list
    '''
    processList = []
    nodeList = []

    proxy = Proxy(c.block_list)
    for i in range(0, c.n):
        nodeList.append(Node(i, '1'))
    pro = Process(target=tFunction_proxy, args=(c.proxy_to_server, c.server_to_proxy, c.stash_size, nodeList, proxy, c.block_list))
    processList.append(pro)
    cli = Process(target=tFunction_client, args=(c.server_to_client, c.client_to_server, len(c.block_list), c.dummy_size, nodeList))
    processList.append(cli)
    for i in range(0, c.n):
        pro = Process(target=tFunction_server, args=(c.proxy_to_server, c.server_to_proxy, c.server_to_client, c.client_to_server, nodeList, nodeList[i]))
        processList.append(pro)

    return processList




def main():
    '''
    System Start.
    The default block list (for test) is ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999'].
    :return: None
    '''
    print('System Start.')

    c.generate_random_block(c)  # Enable this function will randomize the block list.

    processList = init()
    run(processList)

