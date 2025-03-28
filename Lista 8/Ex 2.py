# 2. Abertura Segura de Arquivo
# Escreva um programa que solicite ao usuário o nome de um arquivo para leitura. O
# programa deve tentar abrir o arquivo e exibir seu conteúdo. Utilize tratamento de
# exceções para lidar com a ausência do arquivo e outros possíveis erros.


nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:\n", conteudo)
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao abrir o arquivo: {e}")