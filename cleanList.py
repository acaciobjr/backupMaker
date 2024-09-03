
arquivo_entrada = 'arquivo.txt'
arquivo_saida = 'arquivo_limpo.txt'

# Lê todas as palavras do arquivo, removendo duplicatas e preservando a ordem
with open(arquivo_entrada, 'r', encoding='utf-8') as file:
    palavras = file.readlines()
    palavras_unicas = list(dict.fromkeys(palavras))

numero_palavras = len(palavras_unicas)

palavras_unicas.append(f'\nLista do {arquivo_entrada} limpa com {numero_palavras} nomes.\n')

# Escreve as palavras únicas de volta no arquivo de saída
with open(arquivo_saida, 'w', encoding='utf-8') as file:
    file.writelines(palavras_unicas)

print(f"Palavras duplicadas removidas. O resultado foi salvo em '{arquivo_saida}'.")
