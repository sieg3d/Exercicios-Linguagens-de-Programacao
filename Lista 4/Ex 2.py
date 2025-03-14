# 2. Encontrar o Maior e o Menor Número

numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if numeros:
    maior = numeros[0]
    menor = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
else:
    print("Nenhum número foi inserido.")