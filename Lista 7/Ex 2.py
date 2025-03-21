# 2. Contagem de Caracteres em uma Palavra
# Escreva um programa que solicite ao usuário uma palavra e utilize um dicionário para armazenar a contagem de cada caractere presente na palavra.
# Exiba o dicionário ao final.

palavra = input("Digite uma palavra: ")
contagem_caracteres = {}

for caractere in palavra:
    contagem_caracteres[caractere] = contagem_caracteres.get(caractere, 0) + 1

print("Contagem de caracteres:", contagem_caracteres)