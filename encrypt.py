import IO
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

"""
    Method to obtain the public key that is in a file (str --> key object)
    pubKeyFile: File that contains the public key 
"""
def getPublicKey(pubKeyFile):
    with open(pubKeyFile, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
        return public_key

"""
    Method to encrypt a text based on it's public key
    message: Text to encrypt
    public_key: Public key 
"""
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

    message=IO.readText(raw_input("Enter file text to encrypt: "))
    publicKey=getPublicKey(raw_input("Enter publicKey file: "))
    output=raw_input("Enter file destination of encrypted text: ")
    output=output.strip()
    if(output==""):
        output="files/encrypted.txt"

    encrypted_mess=encrypt(message,publicKey)

    IO.generateFile(encrypted_mess, output)







