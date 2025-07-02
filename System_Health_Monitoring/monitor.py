import psutil

def get_system_metrics():
    print("CPU Usage:", psutil.cpu_percent(), "%")
    print("RAM Usage:", psutil.virtual_memory().percent, "%")
    print("Disk Usage:", psutil.disk_usage('/').percent, "%")
    print("System Uptime:", psutil.boot_time())

get_system_metrics()
