"""
Curso em video

Lê cinco números e informa o maior e o menor com suas posições.
"""

valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}° valor: ')))

maior = max(valores)
menor = min(valores)
posicao_maior = valores.index(maior)
posicao_menor = valores.index(menor)

print(f'O maior valor é o {maior} e está na {posicao_maior+1}° posição')
print(f'O menor valor é o {menor} e está na {posicao_menor+1}° posição')
