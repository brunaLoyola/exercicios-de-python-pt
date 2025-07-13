"""
Curso em video: Preços em Tuplas

Exibe uma lista de produtos com seus preços organizados em formato tabular
"""

produtos = ('Macarrão', 5.99, 'Arroz', 18.99, 'Feijão', 5.99)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]}: ', end='')
    else:
        print(f'R$ {produtos[pos]}')
