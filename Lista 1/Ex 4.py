# 4. Cálculo do Salário Mensal
# Faça um programa que pergunte o número de horas trabalhadas no mês e o valor recebido
# por hora. O programa deve calcular e exibir o salário total do mês.


ht = float(input("Digite as horas trabalhadas:"))
vr = float(input("Digite o valor recebido por hora:"))

recebimento = ht * vr

print(f"O valor total recebido é R${recebimento}")