"""
Exercício:

Receba informações do usuário, converta os tipos
exiba o tipo de cada variável.
"""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura'))

print(type(nome))
print(type(idade))
print(type(altura))

print(f'{nome} tem {idade} anos e mede {altura} metros')
