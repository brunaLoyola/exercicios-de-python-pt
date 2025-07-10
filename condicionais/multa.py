""""
Curso em video: Valor multa

Lê a velocidade de um carro e informa se houve multa
com base no limite de 80 km/h.
"""

velocidade = int(input('Digite a sua velocidade km/h: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(
        f'Sua velocidade é de {velocidade}km/h\n'
        f'Você ultrapassou os limites permitidos, sua multa é de R${multa:.2f}'
    )
else:
    print(f'Sua velocidade é {velocidade}km/h. Parabéns você está no limite.')
