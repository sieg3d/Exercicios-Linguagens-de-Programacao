# 3. Listagem de Cores do Arco-Íris
# Crie uma tupla contendo as cores do arco-íris em ordem. Depois, permita que o usuário informe um número de 1 a 7 e exiba a cor correspondente.

cores_arco_iris = ('vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta')

numero = int(input("Digite um número de 1 a 7: "))

if 1 <= numero <= 7:
    print(f"A cor correspondente é {cores_arco_iris[numero - 1]}.")
else:
    print("Número inválido. Digite um número de 1 a 7.")