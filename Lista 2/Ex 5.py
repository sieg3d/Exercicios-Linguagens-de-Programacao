# 5. Verificação de Triângulo
# Peça ao usuário três números representando os lados de um triângulo. O programa deve
# verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
# sempre maior que o terceiro).

lado1 = int(input("Digite o primeiro lado do triangulo:"))
lado2 = int(input("Digite o segundo lado do triangulo:"))
lado3 = int(input("Digite o terceiro lado do triangulo:"))

if(lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1):
    print("Triangulo valido")
else:
    print("Triangulo invalido")