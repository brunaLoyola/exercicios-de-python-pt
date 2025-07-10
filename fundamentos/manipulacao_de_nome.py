"""
Exercício:

Manipulação e análise de nomes.
"""

nome_completo = input('Digite seu nome completo: ')

maiuscula = nome_completo.upper()
minuscula = nome_completo.lower()

print(f'Esse é seu nome com letra maiúscula: {maiuscula}.')
print(f'Esse é seu nome com letra minúscula: {minuscula}.')

nome_sem_espaco = len(minuscula.replace(' ', ''))

print('Quantidade de letras no seu nome completo: ', nome_sem_espaco)

nome_lista = nome_completo.split()
print(
    f'Seu primeiro nome é {nome_lista[0]}\n'
    f'Seu nome tem {len(nome_lista[0])}'
)
