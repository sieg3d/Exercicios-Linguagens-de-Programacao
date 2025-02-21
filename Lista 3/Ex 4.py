# 4. Números Ímpares em um Intervalo
# Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
# exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem
# ímpares).

A = int(input("Digite o início do intervalo (A): "))
B = int(input("Digite o fim do intervalo (B): "))
for i in range(A, B + 1):
    if i % 2 != 0:
        print(i)
