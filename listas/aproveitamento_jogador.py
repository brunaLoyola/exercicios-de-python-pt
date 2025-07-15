"""
Curso em video: Aproveitamento de jogador

Gerencia o aproveitamento de um jogador de futebol, armazenando
nome, partidas e gols em um dicionário.
"""

jogador = {}
gols = []

jogador['Nome'] = input('Nome do Jogador: ')
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))

for i in range(total):
    gols.append(int(input(f'Quantos gols foram feitos na {i + 1}° partida: ')))

jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)

print(jogador)

print('-=' * 30)

for k, v in jogador.items():
    print(f'No campo {k} tem o valor {v}')

print('-=' * 30)

print(f'O jogador {jogador["Nome"]}, jogou {len(jogador["Gols"])} partidas')

for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["Total"]}')
