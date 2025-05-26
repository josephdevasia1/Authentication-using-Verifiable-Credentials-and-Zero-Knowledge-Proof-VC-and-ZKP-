from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import json

# Generate RSA key pair (Issuer)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Sample Verifiable Credential
vc = {
    "id": "vc-12345",
    "subject": {
        "name": "Alice",
        "dob": "2001-01-01"
    },
    "issuer": "GovID Authority",
    "type": ["VerifiableCredential", "IDCredential"]
}

# Sign the credential
vc_bytes = json.dumps(vc).encode()
signature = private_key.sign(vc_bytes, padding.PKCS1v15(), hashes.SHA256())

# Save credential and signature
with open("vc.json", "w") as f:
    json.dump({"credential": vc, "signature": signature.hex()}, f)

# Save public key
with open("issuer_public.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
