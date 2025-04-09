## 📜 Python Script

#File: `log_monitor.py`

```python
import time
import re
import smtplib
from email.mime.text import MIMEText

# ✅ Function to monitor the log file for successful login events
def monitor_log(file_path, keywords):
    with open(file_path, 'r') as file:
        file.seek(0, 2)  # Move to the end of the file
        print(f"🔍 Monitoring started on {file_path}...")

        while True:
            line = file.readline().strip()
            if not line:
                time.sleep(1)
                continue

            print(f"📄 Read line: {line}")

            for keyword in keywords:
                if re.search(keyword, line, re.IGNORECASE):
                    print(f"🚨 ALERT: Found '{keyword}' in log: {line}")
                    send_email_alert(line)

# ✅ Function to send an email alert for successful login
def send_email_alert(log_line):
    sender_email = "sender_email@gmail.com"  #input here your sender email Address
    receiver_email = "rcv_email@gmail.com" #input here your receive email Address
    app_password = "google app password" #create app password using google account setting____sender email address app password

    username_match = re.search(r"Accepted \S+ for ([\w-]+) from", log_line)
    username = username_match.group(1) if username_match else "Unknown"

    subject = f"✅ Successful Login Alert for {username}"

    email_body = f"""
    <html>
    <body>
        <h2>🚨 Login Alert: Successful Login</h2>
        <p>A successful login was detected for user <b>{username}</b>.</p>
        <p><b>Login Details:</b><br>{log_line}</p>
        <p>Regards,<br><b>Tanmay</b></p>
    </body>
    </html>
    """

    msg = MIMEText(email_body, "html")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"✅ Email alert sent successfully for user: {username}!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    log_file = "/var/log/secure"
    keywords_to_watch = ["Accepted password"]
    monitor_log(log_file, keywords_to_watch)
