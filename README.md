# login_monitoring_in_linux
This project monitors **successful SSH logins** on a Linux system and sends **email alerts** with login details. It continuously tails `/var/log/secure` (or `/var/log/auth.log` on Ubuntu) and triggers an alert whenever a login match is found based on specific keywords.
