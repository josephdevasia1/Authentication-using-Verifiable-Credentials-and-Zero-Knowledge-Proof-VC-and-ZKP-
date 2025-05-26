
# Privacy-Preserving Identity Verification using Verifiable Credentials and Zero-Knowledge Proofs

This project is a Python-based prototype implementing a privacy-preserving identity verification framework using **Verifiable Credentials (VCs)** and simulated **Zero-Knowledge Proofs (ZKPs)**. The system models a decentralized, user-controlled identity architecture where credentials are securely issued, stored, and selectively disclosed without revealing unnecessary personal information.

---

## 🚀 Features

- Issue Verifiable Credentials from a trusted authority.
- Store credentials securely in a local digital wallet.
- Generate Zero-Knowledge Proofs (simulated) for selective attribute verification (e.g., "age > 18").
- Verify credentials and proofs using cryptographic signatures.
- Modular code for issuer, wallet, verifier, and ZKP logic.

---

## 🛠️ Project Structure

```
.
├── issuer.py        # Simulates credential issuance with RSA signing
├── wallet.py        # Handles credential storage, encryption, and ZKP generation
├── verifier.py      # Validates credential and proof authenticity
├── zkp.py           # Simulates ZKP generation and range checking
├── keys/            # Stores generated RSA key pairs
├── user_wallet.json # Example wallet file with stored credentials
```

---

## 🔐 Cryptography

- **RSA 2048-bit** keys for signing and verification
- **SHA-256** for digital signatures
- Credentials stored in JSON format
- Simulated ZKP logic for proof-of-concept (not cryptographically sound)

---

## 🧪 How to Run

1. Install Python 3 and dependencies:
   ```
   pip install cryptography
   ```

2. Run issuer to create keys and issue credential:
   ```
   python issuer.py
   ```

3. Run wallet to store and encrypt credentials:
   ```
   python wallet.py
   ```

4. Run verifier to request and verify proof:
   ```
   python verifier.py
   ```

---

## 📁 Sample Credential Format

```json
{
  "id": "vc-001",
  "subject": {
    "name": "Alice",
    "dob": "2000-01-01"
  },
  "issuer": "GovID Authority",
  "type": ["VerifiableCredential", "IDCredential"],
  "signature": "base64-encoded-signature"
}
```

---

## 👥 Authors

- Joseph Devasia
