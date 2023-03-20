import shuffle as s
from crypto import encrypt, decrypt
import config as c


class Proxy:
    '''
    proxy, logical entity
    '''

    block_list = []
    len = 0
    queryCount = 0
    pi_list = []
    k_pre = ''
    k_new = ''
    local = []

    def __init__(self, block_list):
        self.block_list = block_list
        self.len = len(block_list)
        self.k_pre = c.generate_random_key()
        self.k_new = c.generate_random_key()

    def increase(self, new_block):
        '''
        Unfinished and not enabled.
        :param new_block:
        :return:
        '''
        self.block_list.append(new_block)
        self.len += 1

    def shuffle(self):
        '''
        Shuffle all storage blocks.
        '''
        self.queryCount = 0
        pi = s.fill_pi(len(self.block_list), c.bucket_size)
        self.pi_list.append(pi)
        en_block_list = s.encrypt(self.k_pre, self.block_list)
        shuffled_en_block_list = s.mel_shuffle(en_block_list, pi, self.k_pre, self.k_new, 1)
        self.block_list = decrypt(self.k_new, shuffled_en_block_list)
        self.k_pre = self.k_new
        self.k_new = c.generate_random_key()

    def query(self, i):
        '''
        Query for the block.
        :param i: the index of the block
        :return block: plaintext, type of string
        '''
        pi_location = [j for j in range(len(self.block_list))]
        tmp = [j for j in range(len(self.block_list))]
        for pi in self.pi_list:
            for j in range(len(pi_location)):
                tmp[j] = pi[pi_location[j]]
            pi_location = tmp

        location = [self.block_list[pi_location[j]] for j in range(len(pi_location))]

        self.queryCount += 1
        return location[i]
