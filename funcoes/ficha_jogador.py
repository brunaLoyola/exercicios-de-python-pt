"""
Curso em video: Ficha jogador

Função ficha() que recebe nome e gols de um jogador
como parâmetros opcionais e exibe a ficha formatada.
"""


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')


nome_usuario = input('Nome jogador: ')
quantidade_gols = input('Número de gols: ')

if quantidade_gols.isnumeric():
    quantidade_gols = int(quantidade_gols)
else:
    quantidade_gols = 0
if nome_usuario.strip() == '':
    ficha(gols=quantidade_gols)
else:
    ficha(nome=nome_usuario, gols=quantidade_gols)
