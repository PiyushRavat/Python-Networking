import smtplib
from email.mime.text import MIMEText

body = "This is a test email.How are you"

msg = MIMEText(body)
msg['From'] = "mrsgroup309@gmail.com"
msg['To'] = "sachinsiddhpura007@gmail.com,mrsgroup309@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("mrsgroup309@gmail.com","@@@@@@@@")

server.send_message(msg)

print("Mail sent")

server.quit()

