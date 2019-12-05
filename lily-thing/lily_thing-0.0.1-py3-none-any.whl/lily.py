import re

def strippunc(s):
    return re.sub(r'([^\w\s]|_)+(?=\s|$)', '', s)

