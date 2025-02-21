# 1. Par ou Ímpar?
# Escreva um programa que solicite um número inteiro ao usuário e informe se ele é par ou
# ímpar.

num = int(input("Digite um número: "))

if num %2 == 0:
    print(f"O número digitado é par")
else:
    print(f"O número digitado é impar")