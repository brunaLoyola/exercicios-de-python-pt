"""
Exercício:

Conte a quantidade de vogais em um nome informado pelo usuário.
"""

vogais = 'aeiou'
soma = 0
nome = list(input('Digite seu nome: ').lower())

for contador in nome:
    if contador in vogais:
        soma += 1

print(f'Seu nome possui {soma} vogais.')
