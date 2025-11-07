import psutil
import time
import win32gui
import win32process

# ====== Utility ======
def get_foreground_process_name():
    try:
        hwnd = win32gui.GetForegroundWindow()
        if hwnd:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            proc = psutil.Process(pid)
            return proc.name()
    except:
        return "Unknown"
    return "None"

# ====== Detection Logic ======
def detect_keylogger_process():
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            name = proc.info['name']
            raw_cmdline = proc.info.get('cmdline', [])
            cmdline = ' '.join(raw_cmdline) if isinstance(raw_cmdline, list) else ""

            if ("python" in name.lower()) and (
                "keylog" in cmdline.lower() or
                "pynput" in cmdline.lower() or
                "keyboard" in cmdline.lower()
            ):
                suspicious.append((proc.pid, name, cmdline))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return suspicious

# ====== Main Loop ======
def main_loop():
    print("🛡️ Real-Time Antivirus Scanner Running (Press Ctrl+C to stop)\n")

    try:
        while True:
            print("="*60)
            fg = get_foreground_process_name()
            if fg:
                print(f"[INFO] Foreground App: {fg}")

            suspicious_procs = detect_keylogger_process()
            if suspicious_procs:
                print("\n⚠️ Suspicious Python Process Detected:")
                for pid, name, cmdline in suspicious_procs:
                    print(f"   - PID {pid} | {name}\n     → Command: {cmdline}")
            else:
                print("✅ No Suspicious Activity Detected.")

            print("="*60 + "\n")
            time.sleep(3)

    except KeyboardInterrupt:
        print("\n[!] Real-time Antivirus Monitor Stopped by user.")

if __name__ == "__main__":
    main_loop()
