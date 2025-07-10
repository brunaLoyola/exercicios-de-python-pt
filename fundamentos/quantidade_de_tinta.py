"""
Exercício:

Leia a largura e a altura de uma parede, calcule sua área e
a quantidade de tinta necessária, considerando que 1 litro pinta 2 m².
"""

largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = largura * altura
tinta = area / 2

print(
    f'A largura da sua parede é de {largura:.2f}m.\n'
    f'A altura da sua parede é de {altura:.2f}m.\n'
    f'A área da sua parede é de {area:.2f}m².\n'
    f'Para pintar sua parede é necessário {tinta} litros de tinta.'
)
