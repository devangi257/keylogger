import pygetwindow as gw
import time
from datetime import datetime
from rich.console import Console

console = Console()

def track_windows():
    while True:
        try:
            active_window = gw.getActiveWindow()
            all_windows = gw.getAllTitles()

            timestamp = datetime.now()
            active_title = active_window.title if active_window else 'None'
            open_window_count = len([w for w in all_windows if w.strip()])

            log_active = f"{timestamp} - Active window: {active_title}"
            log_count = f"{timestamp} - Open windows: {open_window_count}"

            with open("logs/keystroke_log.txt", "a") as f:
                f.write(f"\n{log_active}\n{log_count}\n")

            # Terminal colorful output
            console.print(f"[bold green]{timestamp}[/] - 🪟 Active Window: [yellow]{active_title}[/]")
            console.print(f"[bold green]{timestamp}[/] - 📂 Open Windows: [magenta]{open_window_count}[/]")

        except Exception:
            pass
        time.sleep(15)
