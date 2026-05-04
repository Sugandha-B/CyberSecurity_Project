SAFE_PROCESSES = ["chrome", "brave", "firefox", "systemd"]

def analyze_process(proc, config):
    try:
        name = proc.name().lower()

        if name in SAFE_PROCESSES:
            return None

        if proc.cpu_percent() > config.CPU_THRESHOLD:
            return "High CPU usage"

        if proc.memory_info().rss > config.MEMORY_THRESHOLD:
            return "High memory usage"

    except:
        return None

    return None
