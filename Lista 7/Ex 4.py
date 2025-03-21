# 4. Estatísticas de um Texto
# Peça ao usuário para inserir uma frase. Utilize um dicionário para armazenar a contagem de palavras, ou seja, a chave será a palavra e o valor será o número de vezes que ela aparece na frase.
# Exiba o dicionário ao final.

frase = input("Digite uma frase: ").lower()
contagem_palavras = {}

palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print("Contagem de palavras:", contagem_palavras)