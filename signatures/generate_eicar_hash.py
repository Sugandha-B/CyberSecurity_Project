import hashlib
import json

# Read hex file
with open(r"D:\CyberSecurity\samples\test_malware\eicar.hex.txt", "r") as f:
    hex_data = f.read().strip()

# Convert hex -> raw bytes
eicar_bytes = bytes.fromhex(hex_data)

# Generate hashes
hashes = {
    "md5": hashlib.md5(eicar_bytes).hexdigest(),
    "sha1": hashlib.sha1(eicar_bytes).hexdigest(),
    "sha256": hashlib.sha256(eicar_bytes).hexdigest(),
    
}

# Metadata (recommended)
data = {
    "name": "EICAR-Test-File",
    "type": "test-signature",
    "length_bytes": len(eicar_bytes),
    "hashes": hashes
}

# Write JSON
with open("eicar.json", "w") as f:
    json.dump(data, f, indent=4)

print("eicar.json generated successfully")
