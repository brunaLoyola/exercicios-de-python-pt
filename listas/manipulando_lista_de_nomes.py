"""
Exercício:

Manipula uma lista de nomes realizando alterações e verificações.
"""

lista_nomes = ['Bruna', 'Jean', 'Helena', 'Maria', 'Antonio']

print(
    f'O primeiro nome da lista é {lista_nomes[0]}\n'
    f'E o último nome da lista é {lista_nomes[-1]}'
)

lista_nomes[1] = 'Cesar'
print(lista_nomes)

lista_nomes.append('Fernanda')
print(lista_nomes)

lista_nomes.pop(2)
print(lista_nomes)

print(len(lista_nomes))

print('Jean' in lista_nomes)
