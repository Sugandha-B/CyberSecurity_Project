import os
from src.engine.hasher import sha256_file

def scan_directory(path, signatures):
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            file_hash = sha256_file(file_path)
            if not file_hash:
                continue

            if file_hash in signatures:
                sig = signatures[file_hash]
                print(f"[INFECTED] {file_path}")
                print(f"  Name: {sig['name']}\n")
            else:
                print(f"[CLEAN] {file_path}")
