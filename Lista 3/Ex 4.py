# 4. Números Ímpares em um Intervalo
A = int(input("Digite o início do intervalo (A): "))
B = int(input("Digite o fim do intervalo (B): "))
for i in range(A, B + 1):
    if i % 2 != 0:
        print(i)