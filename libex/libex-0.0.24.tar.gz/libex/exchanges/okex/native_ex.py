from datetime import datetime



def init():
    pass

def gen_coid():

    return 'toid' + datetime.now().strftime('%Y%m%d%H%M%S%f')