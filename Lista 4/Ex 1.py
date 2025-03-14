# 1. Soma dos Elementos de uma Lista

numeros = []
while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'fim'.")

if numeros:
    soma = 0
    for numero in numeros:
        soma += numero
    print(f"A soma dos elementos da lista é: {soma}")
else:
    print("Nenhum número foi inserido.")