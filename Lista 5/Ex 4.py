# 4. Inverter a Lista (sem função)

palavras = []
while True:
    entrada = input("Digite uma palavra (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    palavras.append(entrada)

if palavras:
    lista_invertida = palavras[::-1]
    print(f"Lista invertida: {lista_invertida}")
else:
    print("Nenhuma palavra foi inserida.")