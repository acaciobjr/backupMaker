import yagmail

destinatario = 'email de destino'
caminho_zip = 'caminho do seu arquivo.zip'
usuario_gmail = 'email remetente'
senha = 'senha do email remetente'

def enviando_zip_com_yag(destinatario, caminho_zip, usuario_gmail, senha):
    yag = yagmail.SMTP(usuario_gmail, senha)
    yag.send(
        to=destinatario,
        subject="assunto do email",
        contents="texto da mensagem",
        attachments= caminho_zip,
    )

test = enviando_zip_com_yag(destinatario, caminho_zip, usuario_gmail, senha)
