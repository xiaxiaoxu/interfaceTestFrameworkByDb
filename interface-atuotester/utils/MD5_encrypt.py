#encoding=utf-8
import hashlib

def md5_encrypt(text):
    '''md5加密'''
    md5 = hashlib.md5()
    md5.update(text)
    return md5.hexdigest()

if __name__ == '__main__':
    print md5_encrypt("wdx")