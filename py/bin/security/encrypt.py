import os, binascii
from backports.pbkdf2 import pbkdf2_hmac

class PasswordCipher:

    def encrypt(self, raw):
        salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
        passwd = raw.encode("utf8")
        key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32)
        return binascii.hexlify(key)
