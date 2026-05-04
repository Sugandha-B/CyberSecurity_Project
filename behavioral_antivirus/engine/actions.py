import os
import shutil

def kill_process(proc):
    try:
        proc.kill()
        return f"[KILLED] PID {proc.pid}"
    except:
        return "[ERROR] Could not kill process"


def quarantine_file(file_path):
    try:
        quarantine_dir = "quarantine"
        if not os.path.exists(quarantine_dir):
            os.makedirs(quarantine_dir)

        filename = os.path.basename(file_path)
        shutil.move(file_path, os.path.join(quarantine_dir, filename))
        return f"[QUARANTINED] {filename}"
    except:
        return "[ERROR] Could not quarantine file"
