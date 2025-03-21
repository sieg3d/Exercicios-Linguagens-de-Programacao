# 5. Classificação de Times de Futebol
# Crie uma tupla contendo os 10 primeiros colocados de um campeonato de futebol. Depois, exiba:
# • Os três primeiros colocados.
# • Os últimos três colocados.
# • Os times em ordem alfabética.
# • A posição de um time específico informado pelo usuário.

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 
         'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Corinthians')

print("Três primeiros colocados:", times[:3])
print("Três últimos colocados:", times[-3:])
print("Times em ordem alfabética:", sorted(times))

time_informado = input("Digite o nome de um time: ")
if time_informado in times:
    print(f"O {time_informado} está na {times.index(time_informado) + 1}ª posição.")
else:
    print(f"{time_informado} não está na lista dos 10 primeiros.")