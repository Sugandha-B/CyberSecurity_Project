# src/engine/hasher.py - FIXED
import hashlib
import os

def sha256_file(path):
    """Calculate SHA256 hash of a file."""
    h = hashlib.sha256()
    try:
        # Check if file exists and is accessible
        if not os.path.exists(path):
            print(f"[!] File not found: {path}")
            return None
            
        # Check file size
        file_size = os.path.getsize(path)
        if file_size == 0:
            print(f"[!] Empty file: {path}")
            return "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # Empty file hash
        
        with open(path, "rb") as f:
            # Read in chunks for memory efficiency
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()
    except PermissionError:
        print(f"[!] Permission denied: {path}")
        return None
    except Exception as e:
        print(f"[!] Error reading {path}: {e}")
        return None

# Optional: Add multiple hash functions
def hash_file(path, algorithm="sha256"):
    """Calculate hash of a file using specified algorithm."""
    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256
    }
    
    if algorithm not in algorithms:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    h = algorithms[algorithm]()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        print(f"[!] Error calculating {algorithm} for {path}: {e}")
        return None