#!/usr/local/bin/python3
# coding=utf-8



import random
import shuffle as s
from crypto import encrypt, decrypt, aes_encrypt, aes_decrypt
import config as c


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    pi = s.fill_pi(len(c.block_list), c.bucket_size)
    pi = [2, 0, 1, 4, 3, 5, 6, 8, 7, 9]
    print(pi)
    en_block_list = s.encrypt(c.k_pre, c.block_list)
    shuffled_en_block_list = s.mel_shuffle(en_block_list, pi, c.k_pre, c.k_new, 2)
    c.block_list = decrypt(c.k_new, shuffled_en_block_list)
    re = [c.block_list[pi[i]] for i in range(len(c.block_list))]
    print(re)
    #print(c.block_list)
