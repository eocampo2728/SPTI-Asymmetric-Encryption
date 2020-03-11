import IO
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


"""
    Method to generated a pair of keys (public-private) based on
    the given key size.
    keySize: Sizeof the key (>=2048)
"""
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

"""
    Method to save the keys on a file
    pik: Private key
    puk: Public key
"""
def exportKeys(pik, puk):
    print("\nPrivate key")
    IO.generateFile(pik, 'files/keys/privateKey.pem')
    
    print("\nPublic key")
    IO.generateFile(puk, 'files/keys/publicKey.pem')


def main(keySize):
    keyGenerator(keySize)



