# keygen.py

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

def generate_private_key():
    return ec.generate_private_key(ec.SECP384R1())

def derive_shared_secret(private_key, peer_public_key):
    shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
    derived_key = hashes.Hash(hashes.SHA256())
    derived_key.update(shared_key)
    return derived_key.finalize()

pk = generate_private_key()
print(derive_shared_secret(pk, pk.public_key()))
                  