"""
Curso em video: Pessoas e estatísticas

Armazena nome, sexo e idade de várias pessoas em dicionários
dentro de uma lista e exibe estatísticas como média de idade
e lista de mulheres.
"""

grupo = []
pessoa = {}
soma = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = input('Nome: ')
    while True:

        pessoa['Sexo'] = input('Sexo?: [M/F] ').upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro!! Digite uma opção válida')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    grupo.append(pessoa.copy())
    while True:
        continuar = input('Quer continuar: [S/N] ').upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro!! Digite uma opção válida')
    if continuar == 'N':
        break

print(f'Ao todo temos {len(grupo)} pessoas cadastradas')
media = soma / len(grupo)
print(f'A média das idades é {media:5.2f} anos')
print('As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}, ', end='')
print('')
print('Lista das pessoas que estão acima da média: ', end='')
for p in grupo:
    if p['Idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
