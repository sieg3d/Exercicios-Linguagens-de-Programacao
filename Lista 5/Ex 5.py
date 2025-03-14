# 5. Contar Ocorrências de um Elemento

numeros = input("Digite uma lista de números separados por espaço: ")
lista = list(map(int, numeros.split()))

elemento = int(input("Digite o número que deseja contar: "))

contador = 0
for num in lista:
    if num == elemento:
        contador += 1

print(f"O número {elemento} aparece {contador} vezes na lista.")
