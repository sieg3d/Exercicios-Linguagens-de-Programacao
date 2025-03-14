# 3. Remover Duplicatas

numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if numeros:
    lista_sem_duplicatas = []
    for numero in numeros:
        if numero not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(numero)
    print(f"Lista sem duplicatas: {lista_sem_duplicatas}")
else:
    print("Nenhum número foi inserido.")