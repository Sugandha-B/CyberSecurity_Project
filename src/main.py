# src/main.py - FIXED
import os
import sys
import argparse
from src.utils.loader import load_signatures
from src.engine.scanner import scan_directory, scan_file

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Basic Signature-Based Antivirus Scanner')
    parser.add_argument('path', nargs='?', default='.', 
                       help='File or directory to scan (default: current directory)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Show verbose output')
    parser.add_argument('-q', '--quiet', action='store_true',
                       help='Show only infected files')
    parser.add_argument('-t', '--test', action='store_true',
                       help='Run a test scan with sample files')
    
    args = parser.parse_args()
    
    # Print banner
    print("\n" + "="*60)
    print("BASIC SIGNATURE-BASED ANTIVIRUS SCANNER")
    print("="*60 + "\n")
    
    # Load signatures
    print("[*] Loading malware signatures...")
    signatures = load_signatures()
    
    if not signatures:
        print("[!] No signatures loaded. Scanner will not detect anything!")
        print("[!] Make sure you have signature files in the 'signatures/' directory")
        print("[!] Run: python signatures/generate_eicar_hash.py to create test signatures")
        return
    
    # Test mode - scan sample files
    if args.test:
        print("\n[*] Running test scan...")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        samples_dir = os.path.join(project_root, "samples")
        
        if not os.path.exists(samples_dir):
            print(f"[!] Samples directory not found: {samples_dir}")
            print("[*] Creating test sample...")
            os.makedirs(samples_dir, exist_ok=True)
            
            # Create a test EICAR file
            eicar_string = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
            test_file = os.path.join(samples_dir, "eicar_test.com")
            with open(test_file, "wb") as f:
                f.write(eicar_string.encode('utf-8'))
            print(f"[+] Created test file: {test_file}")
        
        return scan_directory(samples_dir, signatures, verbose=args.verbose)
    
    # Normal scan mode
    scan_path = args.path
    
    if not os.path.exists(scan_path):
        print(f"[!] Path not found: {scan_path}")
        return
    
    if os.path.isfile(scan_path):
        # Scan single file
        from src.engine.scanner import scan_file as scan_single_file
        result = scan_single_file(scan_path, signatures)
        
        if result and result.get('infected'):
            print(f"\n[!] INFECTION DETECTED in {scan_path}")
        else:
            print(f"\n[✓] File is clean: {scan_path}")
    else:
        # Scan directory
        return scan_directory(scan_path, signatures, verbose=not args.quiet)

if __name__ == "__main__":
    main()