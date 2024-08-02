# main.py

from keygen import derive_shared_secret, generate_private_key
from encryption import encrypt_message
from signing import sign_message

def secure_communication(message: str, recipient_public_key: object, private_key: object, rsa_private_key: object) -> tuple:
    """Encrypts and signs a message for secure communication with a Telegram bot.

    This function uses a combination of ECDH, ChaCha20, and RSA256 to ensure 
    confidentiality, integrity, and authenticity of the message.

    Args:
      message: The message to be encrypted and signed (string).
      recipient_public_key: The recipient's ECDH public key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicKey).
      private_key: The sender's ECDH private key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey).
      rsa_private_key: The sender's RSA private key for signing (cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey).

    Returns:
      A tuple containing:
        - ciphertext: The encrypted message (bytes).
        - nonce: The nonce used for encryption (bytes).
        - signature: The RSA signature of the ciphertext (bytes).
    """
    # Derive shared secret using ECDH
    shared_secret = derive_shared_secret(private_key, recipient_public_key)

    # Encrypt the message using ChaCha20
    ciphertext, nonce = encrypt_message(message, shared_secret)

    # Sign the ciphertext using RSA256
    signature = sign_message(ciphertext, rsa_private_key)

    return ciphertext, nonce, signature


private_key = generate_private_key()
print(secure_communication("Send this message", private_key.public_key(), private_key, generate_private_key()))