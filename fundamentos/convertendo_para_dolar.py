"""
Curso em video: Conversor de moeda

Converte um valor em reais (R$) fornecido pelo usuário para dólares (U$)
Usando a taxa fixa:
    U$1,00 = R$3,27
"""

dinheiro = float(input('Digite o valor que você tem em sua carteira: '))
conversor = dinheiro / 3.27
print(f'Você pode comprar U${conversor:.3}. ')
