"""
Exercício:

Funções com retorno múltiplo e parâmetros padrão.
Inclui soma, subtração, multiplicação e divisão de dois números
e cálculo da área de um retângulo com valores padrão.
"""


def aritmetica(num01, num02):
    return (
            f'Soma:{num01 + num02} \n Subtração: {num01 - num02} \n'
            f'Multiplicação: {num01 * num02} \n Divisão: {num01 / num02}'
    )


def calcular_area(base, altura):
    if base == altura:
        return print('Isso é um quadrado, não um retângulo')
    elif base <= 0 or altura <= 0:
        return print('Não é possível calcular a área')
    else:
        return print(f'O valor da área do retângulo é de {base * altura}')


numero01_usuario = int(input('Digite o primeiro número: '))
numero02_usuario = int(input('Digite o segundo número: '))

print('Os resultados das operações aritméticas são: \n')
aritmetica(numero01_usuario, numero02_usuario)

base_usuario = int(input('Digite o valor da base: '))
altura_usuario = int(input('Digite o valor da altura: '))
calcular_area(base_usuario, altura_usuario)
