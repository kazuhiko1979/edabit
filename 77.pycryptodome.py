from Crypto.Hash import SHA256
from Crypto.Cipher import AES

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

import Crypto.Random

def main():

    # message = b"This is a Some Text!"
    #
    # hash = SHA256.new()
    # hash.update(message)
    # print(hash.digest())

    # key = b'This is a key123'
    # iv = b'This is an IV456'
    # obj = AES.new(key, AES.MODE_CBC, iv)
    # message = "The answer is no".encode('utf-8')
    # ciphertext = obj.encrypt(message)
    # print(ciphertext)
    #
    # obj2 = AES.new(key, AES.MODE_CBC, iv)
    # print(obj2.decrypt(ciphertext))

    # random_func = Crypto.Random.new().read
    # rsa = RSA.generate(1024, random_func)

    # private_key = rsa.export_key(format='PEM')
    # public_key = rsa.public_key().export_key()
    #
    # message = b"This is a Some Text!"
    # cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    # cipher_text = cipher.encrypt(message)
    #
    # print(cipher_text)
    #
    # cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    # print(cipher.decrypt(cipher_text))

    random_func = Crypto.Random.new().read
    rsa = RSA.generate(1024, random_func)

    private_key = rsa.export_key(format='PEM')
    public_key = rsa.public_key().export_key()

    message = b"This is a Some Text!"
    key = RSA.import_key(private_key)
    hash = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hash)

    # hash = SHA256.new(b"testste")
    key = RSA.import_key(public_key)
    pkcs1_15.new(key).verify(hash, signature)





    return


if __name__ == "__main__":
    main()