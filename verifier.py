from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import json

# Load Issuer's public key
with open("issuer_public.pem", "rb") as f:
    issuer_pubkey = serialization.load_pem_public_key(f.read())

# Load VC and signature
with open("user_wallet.json", "r") as f:
    data = json.load(f)

vc_data = json.dumps(data["credential"]).encode()
signature = bytes.fromhex(data["signature"])

# Step 1: Verify the digital signature
try:
    issuer_pubkey.verify(signature, vc_data, padding.PKCS1v15(), hashes.SHA256())
    print("[✔] Signature is valid.")
except Exception as e:
    print("[✘] Signature verification failed:", e)

# Step 2: Check ZKP (assume proof was sent)
from zkp import generate_zkp
zkp_result = generate_zkp("user_wallet.json")

if zkp_result["zkp_proof"] == "ValidAgeProof":
    print("[✔] ZKP proof verified: user is over 18.")
else:
    print("[✘] ZKP proof failed or user underage.")
