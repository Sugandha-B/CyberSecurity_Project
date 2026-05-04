import threading
from monitors.process_monitor import monitor_processes
from monitors.file_monitor import start_file_monitor
from monitors.network_monitor import start_network_monitor

def main():
    print("=== Behavioral Antivirus Started ===")

    t1 = threading.Thread(target=monitor_processes)
    t2 = threading.Thread(target=start_file_monitor)
    t3 = threading.Thread(target=start_network_monitor)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
