"""
Exercício:

Solicitar dados pessoais e calcular o ano de nascimento
com base na idade.
"""

from datetime import datetime

ano_atual = datetime.now().year

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))

ano_nascimento = ano_atual - idade

print(
    f'Seu nome é {nome}, você tem {idade} anos\n'
    f'Nasceu no ano de {ano_nascimento}, seu peso é {peso}kg'
)
