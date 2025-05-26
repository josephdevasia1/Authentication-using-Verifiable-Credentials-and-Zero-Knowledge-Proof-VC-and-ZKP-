import json
from datetime import datetime

def generate_zkp(vc_file: str) -> dict:
    """Simulate a ZKP proving age > 18 without revealing DOB"""
    with open(vc_file, "r") as f:
        data = json.load(f)
        dob = data["credential"]["subject"]["dob"]
    
    # Calculate age
    birth_year = int(dob.split("-")[0])
    current_year = datetime.now().year
    age = current_year - birth_year

    if age >= 18:
        return {"zkp_proof": "ValidAgeProof", "claim": "Age > 18"}
    else:
        return {"zkp_proof": None, "claim": "Underage"}

# Example usage
if __name__ == "__main__":
    proof = generate_zkp("user_wallet.json")
    print(proof)
