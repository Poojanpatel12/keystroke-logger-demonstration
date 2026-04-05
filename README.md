# keystroke-logger-project

# 🔐 Keystroke Logger Demonstration (Cybersecurity Project)

## 📌 Overview

This project is a **Python-based keylogger demonstration** created for educational and cybersecurity learning purposes. It shows how keystrokes can be captured, logged, and analyzed to understand potential security risks.

---

## 🎯 Features

* ⌨️ Capture keystrokes in real-time
* 🕒 Timestamp-based logging
* 📄 Store logs in a local file (`logs.txt`)
* 🛑 Stop logging using ESC key
* 🔒 Demonstrates system-level security restrictions (macOS permissions)

---

## 🛠️ Tech Stack

* Python 3
* pynput (for keyboard input monitoring)

---

## 📁 Project Structure

```
keystroke-logger-demonstration/
│
├── keylogger.py       # Main script
├── logs.txt           # Output logs (ignored in .gitignore)
├── README.md          # Project documentation
└── requirements.txt   # Dependencies
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/Poojanpatel12/keystroke-logger-demonstration.git
cd keystroke-logger-demonstration
```

### 2. Install dependencies

```
pip install pynput
```

---

## ▶️ Usage

Run the keylogger:

```
python3 keylogger.py
```

* Start typing anywhere on your system
* Press **ESC** to stop logging

---

## 📄 Output

Keystrokes are stored in:

```
logs.txt
```

Example:

```
[2026-04-05 23:10:01] h
[2026-04-05 23:10:02] e
[2026-04-05 23:10:03] l
```

---

## ⚠️ macOS Permission Note

On macOS, you must enable permissions:

* System Settings → Privacy & Security
* Enable:

  * Input Monitoring
  * Accessibility

Without this, the keylogger will not capture keystrokes.

---

## 🔐 Security & Ethical Use

This project is strictly for:

* Educational purposes
* Cybersecurity awareness
* Ethical hacking practice

❌ Do NOT use this on systems without permission.

---

## 🚀 Future Improvements

* 🔐 Encrypt logged data
* 🌐 Web dashboard (Flask/React)
* 📧 Email-based log reporting
* 📊 Real-time monitoring interface

---

## 👨‍💻 Author

**Poojan Patel**

---

## 📜 License

This project is for educational use only.
