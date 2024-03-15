import os
import time
import shutil
import zipfile

def encontrar_diretorio(diretorio_origem):
    if os.path.exists(diretorio_origem):
        return diretorio_origem
    return None

diretorio_origem = 'C:\\'

while True:
    texto = input("Qual é o nome da pasta que você deseja fazer backup? ")
    diretorio_destino = texto.strip()
    print(f"você busca '{diretorio_destino}'")

    tempo_inicio = time.time()
    resultado = encontrar_diretorio(os.path.join(diretorio_origem, diretorio_destino))
    tempo_fim = time.time()

    if resultado:
        tempo_decorrido = tempo_fim - tempo_inicio
        print(f"Foi necessário {tempo_decorrido:.4f} segundos para encontrar o diretório: {resultado}")
        break
    else:
        print(f"{diretorio_destino} não foi encontrado neste computador. Tente novamente.")

Listagem = os.listdir(resultado)
quant = len(Listagem)

caminho_do_desktop = os.path.expanduser('~\Desktop')
pasta='backup'
contador=1
while True:
    nome_pasta = f"{pasta} ({contador})"
    caminhoCompleto = os.path.join(caminho_do_desktop, nome_pasta, texto)
    print(caminhoCompleto)
    if not os.path.exists(caminhoCompleto):
        os.makedirs(caminhoCompleto)
        break
    contador += 1

caminhoDoResultado = os.path.join(caminhoCompleto)
print(f"pasta '{nome_pasta} criada com sucesso com {caminhoDoResultado} dentro dela")

for root, dirs, files in os.walk(resultado):
    for directory in dirs:
        src_dir = os.path.join(root, directory)
        dest_dir = os.path.join(caminhoCompleto, os.path.relpath(src_dir, resultado))
        os.makedirs(dest_dir, exist_ok=True)
    for file in files:
        src_file = os.path.join(root, file)
        dest_file = os.path.join(caminhoCompleto, os.path.relpath(src_file, resultado))
        shutil.copy2(src_file, dest_file)

caminho_zip = f"{caminhoCompleto}.zip"
with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(caminhoCompleto):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, caminhoCompleto))
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            zipf.write(dir_path, os.path.relpath(dir_path, caminhoCompleto))

print(f"Pasta '{nome_pasta}' zipada com sucesso")
