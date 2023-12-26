import os
import shutil
import time

def encontrar_diretorio(diretorioOrigem, pasta_inicial='C:\\'):
    for pasta_atual, subpastas, arquivos in os.walk(pasta_inicial):
        for subpasta in subpastas:
            if subpasta == diretorioOrigem:
                caminho_completo = os.path.join(pasta_atual, subpasta)
                return caminho_completo
    return None

while True:
    texto = input("qual o nome do diretório que você deseja fazer backup?")
    diretorioOrigem = texto.replace(" ", "")
    print(f"Procurando por um diretório '{diretorioOrigem}' na sua máquina")
    tempoInicio = time.time()
    resultado = encontrar_diretorio(diretorioOrigem)
    tempoFim = time.time()

    if resultado:
        tempoDecorrido = tempoFim - tempoInicio
        print(f"Foi necessário {tempoDecorrido:.4f} segundos para encontrar o diretório: {resultado}")
        break
    else:
        print(f"{diretorioOrigem} não foi encontrado neste computador. Tente novamente.")

Listagem = os.listdir(resultado)
quant = len(Listagem)

caminho_do_desktop = os.path.expanduser('~/Desktop')
pasta='backup'
contador=2
while True:
    nome_pasta = f"{pasta} ({contador})"
    caminhoCompleto = os.path.join(caminho_do_desktop, nome_pasta)
    if not os.path.exists(caminhoCompleto):
        os.makedirs(caminhoCompleto)
        break
    contador += 1
print(f"pasta '{nome_pasta} criada com sucesso")

for arquivo in Listagem:
    caminhoInicial = os.path.join(resultado, arquivo)
    caminhoFinal = os.path.join(caminhoCompleto, arquivo)
    shutil.move(caminhoInicial, caminhoFinal)

Listagem2 = os.listdir(caminhoCompleto)
quant2 = len(Listagem2)
if quant2 == quant:
    print(f'{quant} itens em {resultado} e {quant2} em {nome_pasta}.')
    time.sleep(2)
    print('backup realizado com sucesso.')
