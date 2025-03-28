# 4. Acesso a Elementos de uma Lista
# Crie uma lista com cinco números e permita que o usuário informe um índice para
# acessar um valor da lista. Utilize tratamento de exceções para evitar erros caso o
# usuário digite um índice inválido.


lista = [10, 20, 30, 40, 50]

while True:
    try:
        indice = int(input("Digite o índice do elemento que deseja acessar (0 a 4): "))
        valor = lista[indice]
        print(f"O valor no índice {indice} é: {valor}")
        break

    except IndexError:
        print("Índice inválido. Por favor, digite um índice entre 0 e 4.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")