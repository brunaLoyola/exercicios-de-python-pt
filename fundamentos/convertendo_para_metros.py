"""
Curso em video: Conversão de metros para centímetros e milímetros

Converte um valor dado em metros pelo usuário, para as unidades de:
    1 metro = 100 centímetros
    1 metro = 1000 milímetros
"""

metros = int(input('Digite quantos metros irá ser convertido: '))
centimetros = metros * 100
milimetros = metros * 1000

print(
    f'A conversão de {metros} m resulta em: \n'
    f'Centímetros: {centimetros} cm \n'
    f'Milímetros: {milimetros} mm.'
)
