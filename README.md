# 🛡️ Login Monitoring in Linux (Python Automation Project)

This project monitors **successful SSH logins** on a Linux system and sends **email alerts** with login details. It continuously tails `/var/log/secure` (or `/var/log/auth.log` on Ubuntu) and triggers an alert whenever a login match is found based on specific keywords.

> 🚀 Built with Python, SMTP email, regex parsing, and deployed as a `systemd` service for auto-start on boot.

---

## 🔧 Features

- 📈 Real-time log monitoring using Python
- 📨 Email alerts for successful logins (username, IP, method)
- 🔁 Runs continuously in the background as a systemd service
- 🛠️ Easy to configure and extend with custom keywords

---
