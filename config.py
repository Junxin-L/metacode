#!/usr/local/bin/python3
# coding=utf-8
from math import sqrt
import random
from multiprocessing import Queue

# default config parameter


MAX = 10000

n = 20  # the number of servers

proxy_to_server = [Queue(n) for _ in range(n)]
server_to_proxy = [Queue(n) for _ in range(n)]
server_to_client = [Queue(n) for _ in range(n)]
client_to_server = [Queue(n) for _ in range(n)]

qNumber = 10  # the number of query times
blockNumber = 25
k_new = "fhakghfjgwqufjndmnvkjk"
k_pre = "dfjhfkjahkfjfaffffaf"

block_list = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999']

bucket_size = int(sqrt(len(block_list)))
dummy_size = bucket_size


def generate_each_random_block(blocksize=32):
    '''
    Generate a random block.
    :param blocksize: the length of a block, default 1M
    :return key, type of string
    '''

    str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(blocksize):
        str += base_str[random.randint(0, length)]
    return str


def generate_random_block(self, blocksize=32):
    '''
    Randomize the block list.
    :param blocksize: the length of a block, default 1M
    :return: None
    '''
    self.block_list = [self.generate_each_random_block(blocksize) for _ in range(self.blockNumber)]
    self.bucket_size = int(sqrt(len(self.block_list)))
    self.dummy_size = self.bucket_size


def generate_random_key(randomlength=16):
    '''
    Generate a random key.
    :param randomlength: the length of key, default 16-length
    :return key, type of string
    '''

    str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        str += base_str[random.randint(0, length)]
    return str


def generate_random_secret_share_index(index, num):
    '''
    Generate a num-length random secret share list for the index.
    :param index: the index of a block, type of int
    :param num: servers number
    :return share list
    '''
    index = int(index)
    random_num = random.sample(range(1, index), k=num - 1)
    random_num.append(0)
    random_num.append(index)
    random_num = sorted(random_num)
    share_list = [random_num[i] - random_num[i - 1] for i in range(1, len(random_num))]

    return share_list


def generate_random_secret_share_block(block, num):
    '''
    Generate a num-length random secret share list for the block.
    :param block: the encrypted block, type of string
    :param num: servers number
    :return share list
    '''
    str_count = 0
    str_len = len(block)
    random_num = random.sample(range(1, str_len), k=num - 1)
    random_num.append(0)
    random_num.append(str_len)
    random_num = sorted(random_num)
    share_list = []
    for i in range(1, len(random_num)):
        _len = random_num[i] - random_num[i - 1]
        share_list.append(block[str_count:str_count + _len])
        str_count += _len

    # share_list = [random_num[i] - random_num[i - 1] for i in range(1, len(random_num))]
    return share_list
