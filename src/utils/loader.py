import json
import os

def load_signatures():
    base = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    sig_dir = os.path.join(base, "signatures")

    signatures = {}

    for file in os.listdir(sig_dir):
        if file.endswith(".json"):
            with open(os.path.join(sig_dir, file)) as f:
                data = json.load(f)
                sha256 = data["hashes"]["sha256"]
                signatures[sha256] = data

    return signatures
