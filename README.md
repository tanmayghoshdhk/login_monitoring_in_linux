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
---
## ▶️ How to Run

Follow these steps to run the project on your Linux machine:

### 1. Clone this repository

git clone https://github.com/tanmayghoshdhk/login_monitoring_in_linux.git
cd login_monitoring_in_linux

### 2. Edit the Python script

Open log_monitor.py and update the following:

    - sender_email: Your Gmail address

    - receiver_email: Your target email address

    - app_password: Your Gmail app password

sender_email = "your-email@gmail.com"
receiver_email = "receiver-email@gmail.com"
app_password = "your-app-password"

### 3. Move Python script to your home directory

mv login_monitor.py /home/your-username/

   - Replace your-username with your actual Linux username.

### 4. Edit the systemd service file

Open login_monitor.service and update the path to match where you moved the Python script:

- ExecStart=/usr/bin/python3 /home/your-username/login_monitor.py
- WorkingDirectory=/home/your-username

### 5. Move the systemd file to the proper location

sudo mv log_monitor.service /etc/systemd/system/

### 6. Enable and start the service

- sudo systemctl daemon-reload
- sudo systemctl enable login_monitor.service
- sudo systemctl start login_monitor.service

### You can check the status with:

## sudo systemctl status login_monitor.service
