"""
Exercício:

Conjunto de funções simples com condicionais e retorno.
Inclui apresentar(), dobro(), multiplica(), eh_par() e boas_vindas().
"""


def apresentar():
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    print(f'Seu nome é {nome} e sua idade {idade} anos')


def dobro(numero):
    return print('O dobro do número é: ', numero * 2)


def multiplica(a, b):
    print(f'{a} x {b} = {a * b}')


def eh_par(numero):
    if numero % 2 == 0:
        print('É par')
    else:
        print('Não é par')


def boas_vindas(nome):
    print(f'Seja bem vindo(a) {nome}')


apresentar()

numero_dobro = int(input('Digite o número: '))
dobro(numero_dobro)

multiplica_primeiro = int(input('Digite o primeiro número: '))
multiplica_segundo = int(input('Digite o segundo número: '))
multiplica(multiplica_primeiro, multiplica_segundo)

par = int(input('Digite um número: '))
eh_par(par)

nome = input('Digite seu nome: ')
boas_vindas(nome)
