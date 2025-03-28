# 1. Divisão Segura
# Crie um programa que solicite ao usuário dois números e realize a divisão do
# primeiro pelo segundo. Utilize tratamento de exceções para evitar erros de
# divisão por zero e erros de entrada inválida (como caracteres não numéricos).


while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
        break

    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")