import IO
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def keyGenerator(keySize):

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=keySize,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    pik = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    puk = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    exportKeys(pik, puk)

def exportKeys(pik, puk):

    IO.generateFile(pik, 'files/keys/privateKey.pem')
    IO.generateFile(puk, 'files/keys/publicKey.pem')
    print("Both keys were saved at files/keys directory")


def main():
    keySize=int(raw_input("Enter key size (>=2048): "))
    keyGenerator(keySize)



