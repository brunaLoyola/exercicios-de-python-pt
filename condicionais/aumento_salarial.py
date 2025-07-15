"""
Curso em video: Aumento salarial

Calcula o aumento salarial com base no valor informado e
nas faixas de reajuste.
"""

salario = float(input('Digite seu salário para o cálculo de aumento: R$'))

if salario <= 1250.00:
    aumento = salario + (salario * 0.15)
    print(f'Seu salário foi de R${salario:.2f}, para R${aumento:.2f}.')
else:
    aumento = salario + (salario * 0.10)
    print(f'Seu salário foi de R${salario:.2f}, para R${aumento:.2f}.')
