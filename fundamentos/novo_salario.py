"""
Curso em video: Aumento de 15% no salário

Leia o salário de um funcionário e mostre o novo valor com 15% de aumento.
"""


salario = float(input('Digite o valor do seu salário: '))
salario_modificado = salario + (salario * 0.15)

print(f'Seu novo salário é de R${salario_modificado:.2f}.')
