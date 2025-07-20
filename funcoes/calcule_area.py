"""
Curso em video: Calcula área

Função área() que recebe as dimensões de um terreno retangular
e exibe sua área calculada.
"""


def area(largura, comprimento):
    total = largura * comprimento
    print(f'Um terreno {largura} X {comprimento} tem área de {total:.2f}m²')


print('Cálculo de Terreno')
largura_usuario = float(input('Largura (m): '))
comprimento_usuario = float(input('Comprimento (m): '))
area(largura_usuario, comprimento_usuario)
