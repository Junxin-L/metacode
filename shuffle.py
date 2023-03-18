import base64
from math import sqrt
import math
import random
from Crypto.Cipher import DES
import binascii

def des_encrypt(message, key):
    key = key.encode('utf-8')
    key = key[:8]
    message = message.encode('utf-8')
    message = message + b"\0" * (8 - len(message) % 8)
    des = DES.new(key, DES.MODE_ECB)
    ciphertext = des.encrypt(message)
    return base64.b64encode(ciphertext).decode()

def des_decrypt(ciphertext, key):
    key = key[:8].encode('utf-8')
    ciphertext = base64.b64decode(ciphertext)
    des = DES.new(key, DES.MODE_ECB)
    message = des.decrypt(ciphertext)
    return message.rstrip(b"\0").decode()

def encrypt(k, i):
    for j in range(len(i)):
        i[j] = des_encrypt(str(i[j]), k)
    return i

def decrypt(k, i):
    for j in range(len(i)):
        i[j] = des_decrypt(str(i[j]), k)
    return i

def k_shuffle(ar):
    """Fisher-Yates Shuffle.
    """
    n = len(ar)
    if n > 0:
        for i in range(n-1):
            j = i + random.randint(0, n-i-1)
            ar[i], ar[j] = ar[j], ar[i]
    return ar
            
def fill_pi(n, size_of_bucket):
    """Shuffle the pi array and return a new pi array.
    """
    size_of_bucket = int(size_of_bucket)
    pi = list(range(n))
    p = []
    for i in range(0, n, size_of_bucket):
        bucket = k_shuffle(pi[i:i+size_of_bucket])
        p += bucket
    return p


def mel_shuffle(i, pi, k1, k2, p):
    """The complete Melbourne shuffle process.
        Input: 
            i: array of n encrypted blocks
            k1: previous key
            k2: new key
            pi: permutation array
        Output: 
            output permuted blocks
    """
    i = decrypt(k1, i)
    
    buckets = sqrt(len(i)) 
    #Let π1 be a random permutation
    pi1 = fill_pi(len(i), buckets)
    i = shuffle_pass(i, pi1, p)
    i = shuffle_pass(i, pi, p)
    return encrypt(k2, i)

def key(i):
    return i[0]

def value(i):
    return i[1]

def shuffle_pass(i, pi, p):
    """One pass of Melbourne shuffle.
    """
    bucket_size = int(sqrt(len(i)))
    ele_per_bucket = math.ceil(len(i) / bucket_size)
    max_elems = p * math.log(len(i))
    rev_bucket = []
    
    # Initialize buckets
    buckets = [[] for _ in range(bucket_size)]
    # Initialize reverse buckets
    rev_bucket = [[] for _ in range(bucket_size)]
    # Initialize bucketM
    bucketM = []
    
    # Distribution phase
    # Step 1: Place each element into its corresponding bucket
    for j in range(len(i)):
        bucket_idx = j // ele_per_bucket
        buckets[bucket_idx].append([j, i[j]])
        
    # Step 2: For each bucket, put the element into its corresponding bucket
    for j in range(bucket_size):
        bucketM = buckets[j]
        for k in range(ele_per_bucket):
            idt = pi[key(bucketM[k])] // ele_per_bucket #The right bucket according to pi
            if idt < len(i):
                rev_bucket[idt].append(bucketM[k])
   
    # Step 3: Padding dummy elements
    #for j in range(bucket_size):
    #    while(len(rev_bucket[j]) < max_elems):
    #        rev_bucket[j].append([-1, -1])
   
    # Clean up phase
    out = []
    re = []
    for b in rev_bucket:
        bm = []
        bm += b
        for j in range(ele_per_bucket):
            if key(b[j]) == -1 : continue #skip dummy elements
            #sort element within bucket according to pi
            idt = pi[key(b[j])] % ele_per_bucket
            bm[idt] = b[j]
        out.append(bm)
    for b in out:
        for ele in b:
            re.append(value(ele))
    return re
