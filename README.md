# 🛡️ Educational Keylogger (Python)

**Author**: Amadu Kamara  
**License**: MIT – Educational use only  
**Status**: In development | Educational tool | Security lab safe  
**Last Updated**: June 2025

---

## 📘 Overview

This Python-based educational keylogger was created to help cybersecurity students understand how basic threat tools operate and how defenders can detect them. It includes ethical use prompts, structured logging, memory-safe threading, and detection guidance.

---

## 🎯 Features

- ✅ Interactive CLI for educational navigation
- ✅ Real-time keystroke logging with timestamp
- ✅ Supports ethical simulation of threat behavior
- ✅ Log file generation or in-memory (volatile) mode
- ✅ Built-in detection analysis and countermeasure tips
- ✅ Simple virtual environment setup with `setup.py`

---

## 🧠 Learning Objectives

- Understand keylogging at the OS level using Python
- Practice detection via log, behavior, and process monitoring
- Learn red team vs. blue team perspectives
- Apply event-driven programming and thread safety

---

## 🔒 Ethical Use Warning

This tool is intended **strictly for educational use**:
> ❗ Do NOT run on any system without explicit permission.  
> ❗ Do NOT use for surveillance, spying, or unauthorized data capture.  

Consent prompt is included to enforce responsible usage.

---

## 🚀 Getting Started

### ✅ Requirements
- Python 3.7+
- Admin or sudo access (keyboard event hook permissions)

### ⚙️ Setup & Run

```bash
# Clone the repo
git clone https://github.com/your-username/educational-keylogger.git
cd educational-keylogger

# Run setup (creates virtualenv & installs keyboard module)
python setup.py

# Windows
venv\Scripts\activate
python educational_keylogger.py

# macOS/Linux
source venv/bin/activate
python educational_keylogger.py
