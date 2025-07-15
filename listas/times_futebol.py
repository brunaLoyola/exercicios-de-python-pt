"""
Curso em video: Campeonato Brasileiro

Exibe dados da Tabela do Campeonato Brasileiro com tupla
contendo os 20 primeiros colocados, mostrando os 5 primeiros,
os 4 últimos, em ordem alfabética e a posição do Bahia.
"""

times = ('Flamengo', 'Cruzeiro', 'Red Bull Bragantino', 'Palmeiras',
         'Fluminense', 'Botafogo', 'Bahia', 'Mirassol', 'Atlético‑MG',
         'Ceará', 'Corinthians', 'Grêmio', 'São Paulo', 'Internacional',
         'Vasco da Gama', 'Vitória', 'Fortaleza', 'Santos',
         'Juventude', 'Sport')

print(f'Os cinco primeiros times são {times[:5]}')
print(f'Os últimos quatro times são {times[-4:]}')
print(f'Ordem alfabética: {sorted(times)}')
print(f'O time Bahia está na posição {times.index('Bahia')+1}')
