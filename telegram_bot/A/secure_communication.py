from keygen import generate_private_key, generate_public_key, derive_shared_secret
from encryption import encrypt_message
from signing import sign_message

def secure_communication(message, recipient_public_key, private_key, rsa_private_key):
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
    # 1. Derive shared secret using ECDH
    shared_secret = derive_shared_secret(private_key, recipient_public_key)

    # 2. Encrypt message with ChaCha20
    ciphertext, nonce = encrypt_message(message, shared_secret)
    
    # 3. Sign the ciphertext with RSA256
    signature = sign_message(ciphertext, rsa_private_key)

    return ciphertext, nonce, signature

private_key = generate_private_key()
print(secure_communication("Send this message", generate_public_key(private_key), private_key, generate_private_key()))