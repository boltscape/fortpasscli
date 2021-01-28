from os import environ
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

iv = b'\x8d\xe0\\\x01\x9dX\xfa\\(/\x0e\x0b\xae\r\xc56'
def enpassword(raw_pass):
    aes = AES.new(b'0P3eRYJPKr5qaIPG5t2OVQEOY98E/VKD', AES.MODE_CBC, iv)
    ct = aes.encrypt(pad(raw_pass.encode("utf-8"), AES.block_size))
    return b64encode(ct).decode('utf-8')

def depassword(rs):
    aes = AES.new(b'0P3eRYJPKr5qaIPG5t2OVQEOY98E/VKD', AES.MODE_CBC, iv)
    for rec in rs:
        rec[1] = (unpad(aes.decrypt(b64decode(rec[1])), AES.block_size)).decode('utf-8')
    return rs
