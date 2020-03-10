import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii

def getPublicKey(pubKeyFile):
    with open(pubKeyFile, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
        return public_key


def readText(textFile):
    f = open(textFile, 'rb')
    message = f.read()
    print(message)
    f.close()
    return message
import binascii

def generateFile(texto, nameFile):
    file = open(nameFile, "w")
    file.write(texto + os.linesep)
    file.close()

def encrypt(message, public_key):
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def main():
    message= readText(raw_input("Ingresa el nombre del archivo de texto a encriptar: "))
    publicKey=getPublicKey(raw_input("Ingresa el nombre del archivo de la llave publica: "))
    
    encrypted_mess=encrypt(message,publicKey)
    print(encrypted_mess)
    generateFile(encrypted_mess, "encrypted.txt")



    

main()   






