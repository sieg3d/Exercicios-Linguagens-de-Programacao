# 2. Operações Matemáticas com Números em uma Tupla
# Solicite ao usuário quatro números inteiros e armazene-os em uma tupla.
# Em seguida, exiba:
# • Quantas vezes o número 9 apareceu na tupla.
# • Em que posição foi digitado o primeiro número 3 (caso exista).
# • Os números pares contidos na tupla.

numeros = tuple(int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(4))

print(f"Números digitados: {numeros}")
print(f"O número 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O primeiro número 3 foi digitado na posição {numeros.index(3)}.")
else:
    print("O número 3 não foi digitado.")

print("Números pares:", tuple(num for num in numeros if num % 2 == 0))