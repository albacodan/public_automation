import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del remitente
from_email = "soporte.seguridad.daa@gmail.com"
from_password = "etzw zrag hbuf muik"

# Configuración del destinatario
#to_email = "danielalbarranacosta610@institutodh.net"
receiver_mail = sys.argv[1].split(',')

# Leer el HTML combinado
with open("send_mail/combined_tables.html", "r") as file:
    html_content = file.read()

# Crear el mensaje de correo electrónico
msg = MIMEMultipart("alternative")
msg["Subject"] = "Tablas Usuarios Locales"
msg["From"] = from_email
#msg["To"] = to_email
msg['To'] = ', '.join(receiver_mail)

# Adjuntar el cuerpo del mensaje en HTML
part = MIMEText(html_content, "html")
msg.attach(part)

# Enviar el correo electrónico
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, receiver_mail, msg.as_string())
    server.quit()
    print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error al enviar el correo: {e}")