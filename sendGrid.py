import sendgrid
import zipfile
import os
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment, FileContent, FileName, FileType, Disposition

#sua chave de API SendGrid
sg = sendgrid.SendGridAPIClient(api_key='YOUR_API_KEY')

from_email = Email("seu_email@gmail.com")
to_email = To("email_destinatario@gmail.com")
subject = "Assunto do E-mail"
content = Content("text/plain", "Este é o conteúdo do e-mail")

#objeto Mail
message = Mail(from_email, to_email, subject, content)

folder_path = input('insira o caminho da pasta que deseja enviar: ')

#nome do arquivo zip
zip_filename = 'backup.zip'

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, folder_path)
            zipf.write(file_path, arcname=arcname)

#anexe a pasta compactada (ZIP) ao e-mail
attachment = Attachment()
attachment.file_content = FileContent("caminho_para_o_arquivo.zip")
attachment.file_name = FileName("arquivo.zip")
attachment.file_type = FileType("application/zip")
attachment.disposition = Disposition("attachment")

message.attachment = attachment

try:
    response = sg.send(message)
    print("pasta enviada com sucesso")
except Exception as e:
    print("Erro ao enviar o e-mail:", e)
