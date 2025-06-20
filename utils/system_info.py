import platform
import socket
import psutil
from datetime import datetime
from rich.console import Console
from rich.table import Table

def get_system_info():
    info = {
        "Time": str(datetime.now()),
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "Disk Usage": f"{psutil.disk_usage('/').percent}%",
        "Battery": f"{psutil.sensors_battery().percent}%" if psutil.sensors_battery() else "No Battery",
    }

    # Save to log file
    with open("logs/system_info.txt", "w") as f:
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

    # Print using rich table
    console = Console()
    table = Table(title="📊 System Information", show_header=True, header_style="bold magenta")

    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    for key, value in info.items():
        table.add_row(key, str(value))

    console.print(table)
