# 2. Soma de Números Positivos
soma = 0
while True:
    num = int(input("Digite um número (negativo para parar): "))
    if num < 0:
        break
    soma += num
print(f"A soma dos números positivos é: {soma}")
