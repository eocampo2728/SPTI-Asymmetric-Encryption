import IO
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

"""
    Method to obtain the private key that is in a file (str --> key object)
    priKeyFile: File that contains the private key 
"""
def getPrivateKey(priKeyFile):
    with open(priKeyFile, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
        return private_key
    
"""
    Method to decrypt a text based on it's private key
    encrypted: Encrypted text
    private_key: Private key 
"""
def decrypt(encrypted, private_key):
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message


def main():
    message=IO.readFromSys()
    privateKey=getPrivateKey("files/keys/privateKey.pem")
    output="files/decrypted.txt"    

    decrypted_mess=decrypt(message,privateKey)

    IO.generateFile(decrypted_mess, output)
    
    return output



