# 5. Sequência de Fibonacci
N = int(input("Digite o número de termos da sequência de Fibonacci: "))
a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b