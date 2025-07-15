"""
Curso em video: Verificando se é triângulo

Lê o comprimento de três retas e verifica se elas podem formar um triângulo.
"""

reta_01 = int(input('Digite o valor da primeira reta: '))
reta_02 = int(input('Digite o valor da segunda reta: '))
reta_03 = int(input('Digite o valor da terceira reta: '))

if (
    reta_01 + reta_02 > reta_03 and
    reta_01 + reta_03 > reta_02 and
    reta_02 + reta_03 > reta_01
):
    print('A soma das retas forma um triângulo.')
else:
    print('Não é possível formar um triângulo.')
