import os
from src.utils.loader import load_signatures
from src.engine.scanner import scan_directory

def main():
    # Project root (CYBERSECURITY/)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Folder to scan
    SAMPLES_DIR = os.path.join(BASE_DIR, "samples")

    print("[*] Loading signatures...")
    signatures = load_signatures()

    print("[*] Starting scan...\n")
    scan_directory(SAMPLES_DIR, signatures)

    print("\n[*] Scan complete.")

if __name__ == "__main__":
    main()
