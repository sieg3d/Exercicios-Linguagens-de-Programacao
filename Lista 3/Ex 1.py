# 1. Contagem Progressiva
# Escreva um programa que peça um número inteiro positivo ao usuário e exiba todos os
# números de 1 até esse número, um por linha.
    
numero = int(input("Digite um número inteiro positivo: "))
for i in range(1, numero + 1):
    print(i)
