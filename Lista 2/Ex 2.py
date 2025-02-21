# 2. Maior Número
# Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
# sejam iguais, exiba uma mensagem informando essa condição.

num1 = float(input("Digite um numero:"))
num2 = float(input("Digite outro numero:"))

if( num1 == num2):
    print("Os numeros são iguais")
elif(num1 < num2):
    print(f"{num2} é o maior número")
else:
    print(f"{num1} é o maior número")