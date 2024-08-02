from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
from keygen import generate_private_key

def encrypt_message(message, key):
    """Encrypts a message using ChaCha20.

    Args:
        message: The message to be encrypted (string).
        key: The encryption key (bytes).

    Returns:
        A tuple containing:
            - ciphertext: The encrypted message (bytes).
            - nonce: The nonce used for encryption (bytes).
    """
    
    message_bytes = message.encode()
    chacha = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    ciphertext = chacha.encrypt(nonce, message_bytes, None)
    return ciphertext, nonce

print(encrypt_message("encyrpted message", generate_private_key()))