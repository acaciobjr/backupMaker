import os
import shutil

def encontrar_diretorio(diretorioOrigem, pasta_inicial='C:\\'):
    for pasta_atual, subpastas, arquivos in os.walk(pasta_inicial):
        for subpasta in subpastas:
            if subpasta == diretorioOrigem:
                caminho_completo = os.path.join(pasta_atual, subpasta)
                return caminho_completo
    return None

while True:
    diretorioOrigem = input("qual o nome do diretório que você deseja fazer backup?")
    print(f"Procurando por um diretório '{diretorioOrigem}' na sua máquina")
    resultado = encontrar_diretorio(diretorioOrigem)

    if resultado:
        print(f"O diretório encontrado: {resultado}")
        break
    else:
        print(f"{diretorioOrigem} não foi encontrado neste computador. Tente novamente.")

caminho_do_desktop = os.path.expanduser('~/Desktop')
pasta='backup'
caminhoCompleto = os.path.join(caminho_do_desktop, pasta)
os.makedirs(caminhoCompleto)

Listagem = os.listdir(resultado)
quant = len(Listagem)
print(f'{quant} itens no diretório')

for arquivo in Listagem:
    caminhoInicial = os.path.join(resultado, arquivo)
    caminhoFinal = os.path.join(caminhoCompleto, arquivo)
    shutil.move(caminhoInicial, caminhoFinal)
    print('backup realizado com sucesso.')

...
