                      
# encryption.py

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt_message(message, shared_secret):
    nonce = os.urandom(16)
    algorithm = algorithms.ChaCha20(shared_secret, nonce)
    cipher = Cipher(algorithm, mode=None)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return ciphertext, nonce

def decrypt_message(ciphertext, nonce, shared_secret):
    algorithm = algorithms.ChaCha20(shared_secret, nonce)
    cipher = Cipher(algorithm, mode=None)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()