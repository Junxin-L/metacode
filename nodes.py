

class Node:
    '''
    Server
    '''
    id = 0
    share_list = []
    request_share = 0

    def __init__(self, id, share_list):
        self.id = id
        self.share_list = share_list


    def put_request(self, share):
        self.request_share = share





