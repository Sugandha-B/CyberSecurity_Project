import hashlib
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HEX_FILE = os.path.join(
    BASE_DIR, "..", "samples", "test_malware", "eicar.hex.txt"
)

OUTPUT_JSON = os.path.join(BASE_DIR, "eicar.json")

with open(HEX_FILE, "r") as f:
    hex_data = f.read().strip()

eicar_bytes = bytes.fromhex(hex_data)

hashes = {
    "sha256": hashlib.sha256(eicar_bytes).hexdigest()
}

data = {
    "name": "EICAR-Test-File",
    "type": "test-signature",
    "hashes": hashes
}

with open(OUTPUT_JSON, "w") as f:
    json.dump(data, f, indent=4)

print("[+] eicar.json generated")


