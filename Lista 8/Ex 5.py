# 5. Operações Bancárias com Tratamento de Erros
# Crie um programa que simule um sistema bancário simples. O saldo inicial do
# usuário é de R$ 1000,00. O programa deve permitir que o usuário insira um valor
# para saque e, caso o valor solicitado seja maior que o saldo disponível, uma
# exceção personalizada deve ser lançada informando que o saldo é insuficiente.

class SaldoInsuficienteError(Exception):
    pass

saldo = 1000.00

while True:
    try:
        saque = float(input("Digite o valor do saque: "))
        if saque > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")

        saldo -= saque
        print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        break

    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico.")