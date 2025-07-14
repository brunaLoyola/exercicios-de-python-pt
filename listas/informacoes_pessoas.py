"""
Curso em video: Peso pessoas

Lê nome e peso de várias pessoas, exibindo o total cadastrado,
os mais pesados e os mais leves.
"""

lista_temporaria = []
lista_principal = []
pesados = leves = 0

while True:
    lista_temporaria.append(input('Digite seu nome: '))
    lista_temporaria.append(float(input('Digite seu peso: ')))

    if len(lista_principal) == 0:
        pesados = leves = lista_temporaria[1]
    else:
        if lista_temporaria[1] > pesados:
            pesados = lista_temporaria[1]
        if lista_temporaria[1] < leves:
            leves = lista_temporaria[1]
    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(lista_principal)} pessoas')
print(f'O maior peso foi de {pesados}Kg. Peso de ', end='')
for pos in lista_principal:
    if pos[1] == pesados:
        print(f'[{pos[0]}] ', end='')
print(f'O menor peso foi de {leves}Kg. Peso de ', end='')
for pos in lista_principal:
    if pos[1] == leves:
        print(f'[{pos[0]}] ', end='')
