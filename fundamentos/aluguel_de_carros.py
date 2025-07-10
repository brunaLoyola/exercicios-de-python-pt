"""
Curso em video: Exercício de cálculo de aluguel de carro.

Calcula o preço total baseado na quantidade de quilometros percorridos.
e dias de alUguel, usando preço fixo por dia e por km.
"""

km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
valor = (km * 0.15) + (dias * 60)

print(f'O carro rodou {km} km e foi utilizado por {dias} dias,'
      f' o valor a pagar é de R${valor:.2f}.')
