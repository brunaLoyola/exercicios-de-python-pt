"""
Curso em video: Classificando triângulos

Verifica o tipo de triângulo formado com base nas medidas dos lados.
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes
"""

reta_01 = int(input('Digite o valor da primeira reta: '))
reta_02 = int(input('Digite o valor da segunda reta: '))
reta_03 = int(input('Digite o valor da terceira reta: '))

if (
    reta_01 + reta_02 > reta_03 and
    reta_01 + reta_03 > reta_02 and
    reta_02 + reta_03 > reta_01
):
    print('A soma das retas formam um triângulo.')
    if reta_01 == reta_02 == reta_03:
        print('Se trata de um triângulo equilátero.')
    elif reta_01 != reta_02 != reta_03 != reta_01:
        print('Se trata de um triângulo escaleno.')
    else:
        print('Se trata de um triângulo isóceles.')
else:
    print('Não é possível formar um triângulo.')
