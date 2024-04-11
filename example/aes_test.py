from Crypto.Cipher import AES
import hashlib

''''
pip3 install pycryptodemo
'''

BS = AES.block_size

def padding(value):
    src = value.encode()
    length = (len(src) + BS) // BS
    plain = bytearray(length * BS)
    for i, byte in enumerate(src):
        plain[i] = byte
    pad = BS - (len(src) % BS)
    for i in range(pad):
        plain[len(src) + i] = pad
    return plain


def aes_ecb_encrypt(encryptKey, value):
    cryptor = AES.new(bytes.fromhex(encryptKey), AES.MODE_ECB)
    ciphertext = cryptor.encrypt(padding(value))
    return ''.join(['%02x' % i for i in ciphertext]).upper()


def aes_ecb_decrypt(encryptKey, encrypted):
    cryptor = AES.new(bytes.fromhex(encryptKey), AES.MODE_ECB)
    decrypted = cryptor.decrypt(bytes.fromhex(encrypted.lower()))
    trim = 0
    if len(decrypted) > 0:
        trim = len(decrypted) - int(decrypted[len(decrypted) - 1])
    return decrypted[:trim].decode("utf-8")


def get_sha1prng_key(key):
    signature = hashlib.sha1(key.encode()).digest()
    signature = hashlib.sha1(signature).digest()
    return ''.join(['%02x' % i for i in signature])[:32]


if __name__ == '__main__':
    print(AES.block_size)
    key = '6d5582423a974b38865c58745a86261b'
    print(len(key))
    content = '{\"daxue\":\"王\"}'

    sha1prng_key = get_sha1prng_key(key)

    print("===========加密=============")
    result = aes_ecb_encrypt(sha1prng_key, content)

    print(result)
    print("===========解密=============")
    print(aes_ecb_decrypt(sha1prng_key, result))
