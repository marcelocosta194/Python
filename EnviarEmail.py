import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "marcelo.costa@cnova.com"
toaddr = "felipe.duarte@cnova.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Teste"
 
body = "Teste mensagem"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('webmail.suanova.com', 25)
server.starttls()
#server.login(fromaddr, "senha ")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()