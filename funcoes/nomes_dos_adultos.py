"""
Exercício:

Função que recebe listas paralelas de nomes e idades,
retornando apenas os nomes com idade maior que 18.
"""


lista_nomes = []
lista_idades = []
maior_idade = []


def nomes_idades(nomes, idades):
    for i in range(len(idades)):
        if idades[i] > 18:
            maior_idade.append(nomes[i])
    return print(maior_idade)


while True:
    nome_usuario = input('Digite seu nome (ou "sair"): ').lower().split()

    if nome_usuario.lower() == 'sair':
        break
    else:
        idade_usuario = int(input('Digite sua idade: '))
        lista_nomes.append(nome_usuario)
        lista_idades.append(idade_usuario)

nomes_idades(lista_nomes, lista_idades)
