# src/engine/scanner.py - FIXED
import os
import time
from src.engine.hasher import sha256_file

def scan_directory(path, signatures, verbose=True):
    """Scan a directory for malware signatures."""
    infected_count = 0
    clean_count = 0
    error_count = 0
    
    print(f"[*] Scanning: {path}")
    
    # Check if path exists
    if not os.path.exists(path):
        print(f"[!] Path does not exist: {path}")
        return
    
    start_time = time.time()
    
    for root, dirs, files in os.walk(path):
        # Skip hidden/system directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip files that can't be read
            if not os.access(file_path, os.R_OK):
                if verbose:
                    print(f"[!] Skipping (no read access): {file_path}")
                error_count += 1
                continue
            
            # Calculate hash
            file_hash = sha256_file(file_path)
            
            if file_hash is None:
                if verbose:
                    print(f"[!] Skipping (hash error): {file_path}")
                error_count += 1
                continue
            
            # Check against signatures
            if file_hash in signatures:
                # Get signature info - FIXED: signatures[file_hash] is already the data dict
                sig_data = signatures[file_hash]
                infected_count += 1
                print(f"\n[✗] INFECTED: {file_path}")
                print(f"    Threat: {sig_data.get('name', 'Unknown')}")
                print(f"    Type: {sig_data.get('type', 'Unknown')}")
                print(f"    SHA256: {file_hash}")
                
                # Optional: Take action (quarantine, delete, etc.)
                # quarantine_file(file_path)
            else:
                clean_count += 1
                if verbose:
                    print(f"[✓] CLEAN: {file_path}")
    
    elapsed_time = time.time() - start_time
    
    print(f"\n{'='*60}")
    print(f"SCAN SUMMARY")
    print(f"{'='*60}")
    print(f"Total files scanned: {infected_count + clean_count + error_count}")
    print(f"  Clean files: {clean_count}")
    print(f"  Infected files: {infected_count}")
    print(f"  Errors/Skipped: {error_count}")
    print(f"Scan time: {elapsed_time:.2f} seconds")
    print(f"{'='*60}")
    
    return {
        "clean": clean_count,
        "infected": infected_count,
        "errors": error_count,
        "time": elapsed_time
    }

def scan_file(file_path, signatures):
    """Scan a single file."""
    if not os.path.exists(file_path):
        print(f"[!] File not found: {file_path}")
        return None
    
    file_hash = sha256_file(file_path)
    
    if file_hash is None:
        print(f"[!] Could not calculate hash for: {file_path}")
        return None
    
    if file_hash in signatures:
        sig_data = signatures[file_hash]
        print(f"\n[✗] INFECTED: {file_path}")
        print(f"    Threat: {sig_data.get('name', 'Unknown')}")
        print(f"    Type: {sig_data.get('type', 'Unknown')}")
        print(f"    SHA256: {file_hash}")
        return {
            "infected": True,
            "file": file_path,
            "hash": file_hash,
            "threat": sig_data.get('name', 'Unknown')
        }
    else:
        print(f"[✓] CLEAN: {file_path}")
        print(f"    SHA256: {file_hash}")
        return {
            "infected": False,
            "file": file_path,
            "hash": file_hash
        }