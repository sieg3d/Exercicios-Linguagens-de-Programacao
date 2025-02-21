# 5. Sequência de Fibonacci
# Escreva um programa que peça ao usuário um número N e exiba os N primeiros termos da
# Sequência de Fibonacci.
    
N = int(input("Digite o número de termos da sequência de Fibonacci: "))
a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b
