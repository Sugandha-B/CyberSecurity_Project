from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from engine.actions import quarantine_file
import time

class FileHandler(FileSystemEventHandler):
    change_count = 0

    def on_modified(self, event):
        if not event.is_directory:
            self.change_count += 1
            print(f"[FILE MODIFIED] {event.src_path}")

            if self.change_count > 10:
                print("[ALERT] Possible ransomware activity!")
                quarantine_file(event.src_path)


def start_file_monitor(path="."):
    observer = Observer()
    handler = FileHandler()
    observer.schedule(handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
