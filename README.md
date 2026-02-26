## 🔐 Simple Log Monitoring IDS

A lightweight Intrusion Detection System (IDS) built with Python.

This project demonstrates foundational log monitoring techniques
and reflects my journey as a Health-first Security Engineer.

---

## 🚀 Features

- IPv4 extraction from log files
- Suspicious IP detection based on configurable threshold
- Automated security report generation
- Clean modular structure
- Safe-for-publication sample data

---

## 📦 Project Structure

```text
health-security-ids/
│
├── main.py
├── sample_access.log
├── logs/              # (ignored - not published)
├── .gitignore
└── README.md
```

---

## ▶ Usage

Run the script:

```bash
python main.py
```

To change the log source, edit the following line in main.py:

```Python
LOG_FILE = "sample_access.log"
```

## 🔐 Security Policy

- This repository contains sample log data only
- Documentation-only IP addresses (RFC5737) are used
- No real infrastructure logs are included
- API keys or secrets must never be committed
- Real logs should be stored in the /logs directory (ignored via .gitignore)

## 🎯 Design Philosophy

Security should be:

- Transparent
- Minimal
- Reproducible
- Safe to share

This project emphasizes responsible public security engineering and safe open-source practices.

## 🌿 Author

Fujishima
Health-first Security Engineer
Protecting health means protecting information.