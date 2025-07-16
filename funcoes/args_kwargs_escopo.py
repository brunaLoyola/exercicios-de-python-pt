"""
Exercício:

Trabalha com parâmetros variados: *args, **kwargs e escopo.
Inclui funções de média, relatório, soma com variável global
e demonstração de variável local.
"""

global_total = 0


def calcular_media(*args):

    media = sum(args) / len(args)
    return print('Média: ', media)


def relatorio(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')


def soma(numero):
    resultado = global_total + numero
    return print(resultado)


relatorio(nome='Bruna', idade=22, filha='Helena', marido='Jean')
calcular_media(10, 5, 2, 6, 15)
soma(int(input('Digite um número: ')))
