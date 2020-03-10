import IO
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def getPrivateKey(priKeyFile):
    with open(priKeyFile, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
        return private_key
    

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
    message=IO.readText(raw_input("Enter file text to decrypt: "))
    privateKey=getPrivateKey(raw_input("Enter privateKey file: "))
    output=raw_input("Enter file destination of decrypted text: ")
    output=output.strip()
    if(output==""):
        output="files/decrypted.txt"

    decrypted_mess=decrypt(message,privateKey)

    IO.generateFile(decrypted_mess, output)



