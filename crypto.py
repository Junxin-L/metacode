#!/usr/local/bin/python3
# coding=utf-8

import base64
from Crypto.Cipher import AES


def aes_encrypt(message, key):
    key = key.encode('utf-8')
    key = key[:16]
    message = message.encode('utf-8')
    message = message + b"\0" * (16 - len(message) % 16)
    des = AES.new(key, AES.MODE_ECB)
    ciphertext = des.encrypt(message)
    return base64.b64encode(ciphertext).decode()


def aes_decrypt(ciphertext, key):
    key = key[:16].encode('utf-8')
    ciphertext = base64.b64decode(ciphertext)
    des = AES.new(key, AES.MODE_ECB)
    message = des.decrypt(ciphertext)
    return message.rstrip(b"\0").decode()


def encrypt(k, i):
    for j in range(len(i)):
        i[j] = aes_encrypt(str(i[j]), k)
    return i


def decrypt(k, i):
    for j in range(len(i)):
        i[j] = aes_decrypt(str(i[j]), k)
    return i
