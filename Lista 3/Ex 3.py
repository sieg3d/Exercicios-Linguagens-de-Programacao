# 3. Tabuada de um Número
# Peça um número inteiro ao usuário e exiba a tabuada desse número de 1 a 10.

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    print(f"{numero_tabuada} x {i} = {numero_tabuada * i}")
