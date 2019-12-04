from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(data, key):
    key = SHA256.new(key.encode('utf-8')).digest()
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = pad(data.encode('utf-8'), AES.block_size)
    return iv + cipher.encrypt(data)

def decrypt(data, key):
    key = SHA256.new(key.encode('utf-8')).digest()
    iv = data[:AES.block_size]
    raw = data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(raw), AES.block_size)
