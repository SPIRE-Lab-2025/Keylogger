# Keylogger Analysis Lab

> **Important Security & Legal Notice**
> 
> This repository contains educational demonstration code only. The included keylogger is designed for **code inspection and defensive testing** in controlled environments. 
> 
> **⚠️ Usage Restrictions:**
> - Never run on systems with real user data or production networks
> - Only use in labs with explicit authorization
> - Test only with dummy accounts and consenting participants

---

## 1) Install dependencies
```bash
pip install -r requirements.txt
```

---

## 2) Run Keylogger (Standalone Test):
```bash
python keylogger.py
```


Open a browser, navigate to websites, and try to log in using **dummy credentials** only; browse some other website, write some dummy texts or chat with friends. After a few seconds, terminate the keylogger process. Locate `keylog_demo.txt` in either the script directory or your Documents folder. Examine the captured output.

## 3.1) Start the detector (antivirus):

Open **Terminal A** in the repo folder and run:
```bash
python antivirus.py
```
Leave Terminal A running; it prints periodic scans and reports suspicious Python processes it finds.

---

## 3.2) Start the keylogger

Open **Terminal B** (same repo folder) and run:
```bash
python keylogger.py
```
The simulator writes synthetic lines to `keylog_demo.txt` for 60 seconds and then exits.

---

## 3.3) Inspect outputs

- **Monitor (Terminal A)** — expected example output:
```
[INFO] Foreground App: <appname>
⚠️ Suspicious Python Process Detected:
  - PID: 1234 | python.exe
    → Command: python simulated_keylogger.py
```

- **Log file (repo folder)** — view synthetic entries:
```bash
# macOS / Linux
cat keylog_demo.txt

# Windows (PowerShell / cmd)
type keylog_demo.txt
```

---

## 6) Cleanup
```bash
# macOS / Linux
rm keylog_demo.txt

# Windows
del keylog_demo.txt
```

## What you will learn from this safe workflow
- How `antivirus.py` behaves when it inspects running Python processes and command lines.
- How a logging-formatted file looks (without ever capturing real keystrokes).
- How to validate detection pipelines in an ethical and safe manner.
