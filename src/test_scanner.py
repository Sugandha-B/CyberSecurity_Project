# test_scanner.py
import os
import sys
import hashlib
import json

def test_setup():
    """Test the entire setup to find issues."""
    print("="*60)
    print("SCANNER DIAGNOSTIC TEST")
    print("="*60)
    
    # 1. Check project structure
    print("\n1. Checking project structure...")
    required_dirs = ["src", "signatures", "samples"]
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"   [✓] {dir_name}/ exists")
        else:
            print(f"   [✗] {dir_name}/ missing")
    
    # 2. Create proper EICAR test file
    print("\n2. Creating EICAR test file...")
    eicar_string = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    eicar_bytes = eicar_string.encode('utf-8')
    
    samples_dir = "samples"
    os.makedirs(samples_dir, exist_ok=True)
    
    eicar_path = os.path.join(samples_dir, "eicar.com")
    with open(eicar_path, "wb") as f:
        f.write(eicar_bytes)
    
    print(f"   [✓] Created {eicar_path}")
    
    # 3. Calculate its hash
    print("\n3. Calculating EICAR hash...")
    eicar_hash = hashlib.sha256(eicar_bytes).hexdigest()
    print(f"   SHA256: {eicar_hash}")
    
    # 4. Create signature file
    print("\n4. Creating signature file...")
    signatures_dir = "signatures"
    os.makedirs(signatures_dir, exist_ok=True)
    
    signature_data = {
        "name": "EICAR-Test-File",
        "type": "test-signature",
        "description": "Standard antivirus test file",
        "hashes": {
            "sha256": eicar_hash,
            "md5": hashlib.md5(eicar_bytes).hexdigest(),
            "sha1": hashlib.sha1(eicar_bytes).hexdigest()
        }
    }
    
    sig_path = os.path.join(signatures_dir, "eicar.json")
    with open(sig_path, "w") as f:
        json.dump(signature_data, f, indent=4)
    
    print(f"   [✓] Created {sig_path}")
    
    # 5. Test the scanner modules directly
    print("\n5. Testing scanner modules...")
    
    # Import and test hasher
    sys.path.insert(0, 'src')
    from engine.hasher import sha256_file
    
    calculated_hash = sha256_file(eicar_path)
    print(f"   Hasher module calculated: {calculated_hash}")
    print(f"   Matches expected? {'✓' if calculated_hash == eicar_hash else '✗'}")
    
    # Test loader
    from utils.loader import load_signatures
    signatures = load_signatures()
    print(f"   Loader found {len(signatures)} signatures")
    
    # 6. Test signature matching
    print("\n6. Testing signature matching...")
    if eicar_hash in signatures:
        print(f"   [✓] EICAR hash found in signatures!")
        print(f"   Threat name: {signatures[eicar_hash].get('name')}")
    else:
        print(f"   [✗] EICAR hash NOT found in signatures!")
        print(f"   Loaded hashes: {list(signatures.keys())[:2] if signatures else 'None'}")
    
    # 7. Create a clean test file
    print("\n7. Creating clean test file...")
    clean_path = os.path.join(samples_dir, "clean.txt")
    with open(clean_path, "w") as f:
        f.write("This is a clean file for testing.")
    
    clean_hash = sha256_file(clean_path)
    print(f"   Clean file hash: {clean_hash}")
    
    if clean_hash in signatures:
        print(f"   [✗] ERROR: Clean file detected as malware!")
    else:
        print(f"   [✓] Clean file correctly not detected as malware")
    
    print("\n" + "="*60)
    print("DIAGNOSTIC COMPLETE")
    print("="*60)
    
    if eicar_hash in signatures:
        print("\n[✓] SETUP CORRECT! Run the scanner with:")
        print("    python -m src.main --test")
        print("    or")
        print("    python -m src.main samples/")
    else:
        print("\n[✗] SETUP HAS ISSUES!")
        print("    Check the errors above and fix them.")

if __name__ == "__main__":
    test_setup()