import smtplib
import zipfile
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from_email = input('digite seu email: ')
to_email = input('digite o email destinatário: ')
password = input('digite sua senha: ')

#caminho do diretório que deseja enviar
folder_path = input('insira o caminho da pasta que deseja enviar: ')

zip_filename = 'backup.zip'

with open(zip_filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())

#configuração do e-mail
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = 'Assunto do E-mail'

#anexando arquivo zip a email
attachment = open(zip_filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % zip_filename)
msg.attach(part)

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
except Exception as e:
    print("Erro ao conectar no servidor: ", e)

#os.remove(zip_filename)
