# src/utils/loader.py - FIXED
import json
import os

def load_signatures():
    """Load all malware signatures from JSON files."""
    # Get project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    sig_dir = os.path.join(project_root, "signatures")
    
    print(f"[*] Loading signatures from: {sig_dir}")
    
    signatures = {}
    
    # Check if signatures directory exists
    if not os.path.exists(sig_dir):
        print(f"[!] Signatures directory not found: {sig_dir}")
        print(f"[!] Current directory: {os.getcwd()}")
        return signatures
    
    # List all JSON files
    json_files = [f for f in os.listdir(sig_dir) if f.endswith('.json')]
    print(f"[*] Found {len(json_files)} signature files")
    
    for file in json_files:
        file_path = os.path.join(sig_dir, file)
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Extract SHA256 hash
            sha256_hash = data.get("hashes", {}).get("sha256")
            
            if sha256_hash:
                signatures[sha256_hash] = data
                print(f"[+] Loaded signature: {data.get('name', 'Unknown')}")
                print(f"    File: {file}")
                print(f"    SHA256: {sha256_hash[:16]}...")
            else:
                print(f"[!] No SHA256 hash found in {file}")
                
        except json.JSONDecodeError as e:
            print(f"[!] Error parsing JSON in {file}: {e}")
        except Exception as e:
            print(f"[!] Error loading {file}: {e}")
    
    print(f"\n[*] Total signatures loaded: {len(signatures)}")
    
    # Debug: Print loaded hashes
    if signatures:
        print("\n[*] First few loaded hashes:")
        for i, (hash_val, sig_data) in enumerate(list(signatures.items())[:3]):
            print(f"  {i+1}. {hash_val[:16]}... -> {sig_data.get('name', 'Unknown')}")
    
    return signatures

def add_signature(signature_file):
    """Add a new signature from a JSON file."""
    try:
        with open(signature_file, 'r') as f:
            data = json.load(f)
        
        sha256_hash = data.get("hashes", {}).get("sha256")
        if not sha256_hash:
            print("[!] No SHA256 hash in signature file")
            return False
        
        # Save to signatures directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        sig_dir = os.path.join(project_root, "signatures")
        
        # Create if doesn't exist
        os.makedirs(sig_dir, exist_ok=True)
        
        # Generate filename from threat name
        threat_name = data.get('name', 'unknown').replace(' ', '_').lower()
        output_file = os.path.join(sig_dir, f"{threat_name}.json")
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"[+] Signature added: {output_file}")
        return True
        
    except Exception as e:
        print(f"[!] Error adding signature: {e}")
        return False