"""
Curso em video: Boletim escolar

Lê nome e duas notas de vários alunos, armazena em lista
composta e exibe boletim com médias individuais.
"""


ficha = []
while True:
    nome = input('Digite seu nome: ')
    nota01 = float(input('Digite sua primeira nota: '))
    nota02 = float(input('Digite sua segunda nota: '))
    media = (nota01 + nota02) / 2
    ficha.append([nome, [nota01, nota02], media])

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if opcao == 999:
        print('Finalizando...')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
