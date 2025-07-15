"""
Curso em video: Aproveitamento de jogadores

Gerencia aproveitamento de vários jogadores, armazenando
dados em dicionários e permitindo visualização detalhada.
"""
time = []
jogador = {}
gols = []

while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do Jogador: ')
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    gols.clear()
    for i in range(total):
        gols.append(
            int(input(f'Quantos gols foram feitos na {i + 1}° partida: '))
        )

    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        continuar = input('Quer continuar: [S/N] ').upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro!! Digite uma opção válida')
    if continuar == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f' {k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro!! Não existe jogador com código {busca}!')
    else:
        print(f'Levantamento do jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f' No jogo {i+1} fez {g} gols')
