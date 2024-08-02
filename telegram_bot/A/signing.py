from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def sign_message(message, private_key):
    """Signs a message using RSA256.

    Args:
        message: The message to be signed (bytes).
        private_key: The RSA private key for signing (cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey).

    Returns:
        The RSA signature of the message (bytes).
    """
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature