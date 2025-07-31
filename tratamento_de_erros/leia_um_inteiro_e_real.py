"""
Curso em vídeo: Ler um número inteiro e real, fazendo o tratamento de exceções

Função leia_int() que simula input() com tratamento de exceções,
aceitando apenas valores numéricos inteiros.
Função leia_float() que simula input() com tratamento de exceções,
aceitando apenas valores numéricos reais.
"""


def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('Erro!! Por favor, digite um número inteiro')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return valor


def leia_float(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('Erro!! Por favor, digite um número real')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar nenhum número')
            return 0
        else:
            return valor


num01 = leia_int('Digite um número inteiro: ')
num02 = leia_float('Digite um número real: ')

print(f'O valor inteiro digitado foi {num01} e o valor real foi {num02}.')
