"""
Exercício:

Classifica a idade e a nota do usuário para determinar o status final.
"""

idade = int(input('Digite sua idade: '))

if idade >= 0 and idade <= 12:
    print('Você é uma criança.')
elif idade >= 13 and idade <= 17:
    print('Você é um adolescente.')
elif idade >= 18:
    print('Você é um adulto.')
else:
    print('Idade inexistente.')

nota = float(input('Digite sua de 0 a 10: '))

if nota >= 7:
    print('Você está aprovado.')
elif nota >= 5 and nota <= 6.9:
    print('Você está de recuperação.')
elif nota >= 0 and nota < 5:
    print('Você está reprovado.')
else:
    print('Nota inexistente.')
