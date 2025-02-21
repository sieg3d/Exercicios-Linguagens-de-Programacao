# 4. Cálculo de Média e Aprovação
# Elabore um programa que solicite duas notas ao usuário e calcule a média. Em seguida,
# informe se o aluno foi:
# • Aprovado (média maior ou igual a 7)
# • Recuperação (média entre 5 e 6.9)
# • Reprovado (média abaixo de 5)

av1 = float(input("Digite a nota da AV1:"))
av2 = float(input("Digite a nota da AV2:"))
media = (av1 + av2) / 2

print(f"Sua média foi {media}")
if(media >= 7):
    print("Aprovado")
elif(media >= 5 and media < 7):
    print("Recuperação")
elif(media < 5):
    print("Reprovado")