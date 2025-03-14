#2. Verificação de Número Primo

def verificar_primo(numero):
    """Verifica se um número é primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Programa principal
numero = int(input("Digite um número inteiro para verificar se é primo: "))
if verificar_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")