import smtplib
import zipfile
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#comercial.dr02@gmail.com / 159357cdf
# Configurações de e-mail
from_email = input('digite seu email: ')
to_email = input('digite o email destinatário: ')
password = input('digite sua senha: ')

# Caminho para a pasta que você deseja enviar
#C:\Users\Rose\Desktop\backup
folder_path = input('insira o caminho da pasta que deseja enviar: ')

# Nome do arquivo zip
zip_filename = 'backup.zip'

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, folder_path)
            zipf.write(file_path, arcname=arcname)

#Configuração do e-mail
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = 'Assunto do E-mail'

#Anexe o arquivo zip ao e-mail
attachment = open(zip_filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % zip_filename)
msg.attach(part)

# Conecte-se ao servidor SMTP do Gmail e envie o e-mail
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
except:
    print('não foi possível conectar ao servidor SMTP')

# Exclua o arquivo zip após o envio
#os.remove(zip_filename)
