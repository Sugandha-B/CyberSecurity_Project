# signatures/generate_eicar_hash.py - FIXED
import hashlib
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HEX_FILE = os.path.join(BASE_DIR, "..", "samples", "test_malware", "eicar.hex.txt")
OUTPUT_JSON = os.path.join(BASE_DIR, "eicar.json")

# First, let's check what's in the hex file
print(f"[*] Reading hex file from: {HEX_FILE}")
with open(HEX_FILE, "r") as f:
    hex_data = f.read().strip()

print(f"[*] Hex data length: {len(hex_data)} chars")
print(f"[*] First 100 chars: {hex_data[:100]}...")

try:
    # Convert hex to bytes
    eicar_bytes = bytes.fromhex(hex_data)
    print(f"[*] Converted to {len(eicar_bytes)} bytes")
    
    # Try to decode to see what we have
    try:
        decoded = eicar_bytes.decode('utf-8')
        print(f"[*] Decoded string: {repr(decoded)}")
        print(f"[*] String length: {len(decoded)} characters")
    except:
        print("[*] Cannot decode as UTF-8")
    
except ValueError as e:
    print(f"[!] ERROR converting hex to bytes: {e}")
    print("[!] Hex data might be corrupted")
    
    # Create proper EICAR bytes as fallback
    eicar_string = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    eicar_bytes = eicar_string.encode('utf-8')
    print("[*] Using built-in EICAR string instead")
    print(f"[*] EICAR string: {repr(eicar_string)}")

# Generate hashes
hashes = {
    "sha256": hashlib.sha256(eicar_bytes).hexdigest(),
    "md5": hashlib.md5(eicar_bytes).hexdigest(),  # Add MD5 for verification
    "sha1": hashlib.sha1(eicar_bytes).hexdigest()   # Add SHA1 for verification
}

# Print for verification
print(f"\n[*] Generated Hashes:")
print(f"  SHA256: {hashes['sha256']}")
print(f"  MD5:    {hashes['md5']}")
print(f"  SHA1:   {hashes['sha1']}")

print(f"\n[*] Expected EICAR Hashes (Official):")
print(f"  SHA256: 275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f")
print(f"  MD5:    44d88612fea8a8f36de82e1278abb02f")
print(f"  SHA1:   3395856ce81f2b7382dee72602f798b642f14140")

# Check if matches
if hashes['sha256'] == "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f":
    print("\n[✓] SHA256 hash matches official EICAR hash!")
else:
    print("\n[✗] SHA256 hash does NOT match official EICAR hash!")

# Save to JSON
data = {
    "name": "EICAR-Test-File",
    "type": "test-signature",
    "description": "Standard antivirus test file",
    "hashes": hashes
}

with open(OUTPUT_JSON, "w") as f:
    json.dump(data, f, indent=4)

print(f"\n[+] eicar.json generated at: {OUTPUT_JSON}")

# Also create a test file for scanning
test_file = os.path.join(BASE_DIR, "..", "samples", "eicar_test.com")
with open(test_file, "wb") as f:
    f.write(eicar_bytes)
print(f"[+] Test file created at: {test_file}")