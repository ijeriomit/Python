from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

# Pre-shared curve parameters (example using SECP256R1)
curve = ec.SECP256R1()

def generate_private_key():
    """Generates an ECDH private key.

    Returns:
        An ECDH private key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey).
    """
    return ec.generate_private_key(curve)


def generate_public_key(private_key):
    """Generates an ECDH public key from a given private key.

    Args:
        private_key: An ECDH private key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey).

    Returns:
        An ECDH public key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicKey).
    """
    return private_key.public_key()


def derive_shared_secret(private_key, peer_public_key):
    """Derives a shared secret using ECDH.

    Args:
        private_key: Your ECDH private key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey).
        peer_public_key: The other party's ECDH public key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicKey).

    Returns:
        The shared secret (bytes).
    """
    shared_secret = private_key.exchange(ec.ECDH(), peer_public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
    ).derive(shared_secret)
    return derived_key
                  