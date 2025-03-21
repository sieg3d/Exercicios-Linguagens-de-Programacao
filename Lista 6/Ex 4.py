# 4. Nomes de Alunos e Notas
# Crie uma tupla que armazene o nome de cinco alunos e suas respectivas notas (ex: ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)). Depois, exiba apenas os nomes dos alunos e, em seguida, apenas as notas.

alunos_notas = ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)

nomes = alunos_notas[::2]
notas = alunos_notas[1::2]

print("Nomes dos alunos:", nomes)
print("Notas dos alunos:", notas)
