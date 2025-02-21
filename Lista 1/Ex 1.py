# 1. Cálculo da Área do Círculo
# Escreva um programa que peça ao usuário o valor do raio de um círculo e calcule sua área.
# Use a fórmula:

import math
raio = float(input("Digite o raio:"))
area = math.pi * (raio**2)

print(f"A área é: {area}")