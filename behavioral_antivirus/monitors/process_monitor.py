import psutil
import time
from engine.analyzer import analyze_process
from engine.actions import kill_process
import config

known = set()

def monitor_processes():
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.pid not in known:
                print(f"[NEW] {proc.info['name']} ({proc.pid})")
                known.add(proc.pid)

            reason = analyze_process(proc, config)

            if reason:
                print(f"[ALERT] {proc.pid} → {reason}")
                print(kill_process(proc))

        time.sleep(config.MONITOR_INTERVAL)
