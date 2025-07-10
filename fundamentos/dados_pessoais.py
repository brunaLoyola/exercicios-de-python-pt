"""
Exercício:

Armazene dados pessoais e frutas favoritas e exiba as
informações ao final.
"""


frutas_favoritas = []

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

for i in range(1, 4):
    fruta = input(f'Digite a {i}° fruta favorita: ')
    frutas_favoritas.append(fruta)

dados = {
    'nome': nome,
    'idade': idade,
    'altura': altura,
    'frutas_favoritas': frutas_favoritas
}

for chave, valor in dados.items():
    print(f'{chave.capitalize()} : {valor}.')
