import shutil
import smtplib
from email.mime.text import MIMEText

def send_alert(disk, percent):
    msg = MIMEText(f"Alerta: El uso del disco en {disk} ha alcanzado el {percent}%")
    msg['Subject'] = f'Alerta de espacio en disco'
    msg['From'] = 'tu-email@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('tu-email@example.com', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

def check_disk_usage(threshold):
    total, used, free = shutil.disk_usage('/')
    percent_used = (used / total) * 100
    if percent_used > threshold:
        send_alert('/', percent_used)

check_disk_usage(80)
