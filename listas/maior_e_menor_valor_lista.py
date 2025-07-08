"""
Curso em video

Lê cinco números e informa o maior e o menor com suas posições.
"""

valores = []
posicao_maior = []
posicao_menor = []

for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}° valor: ')))

maior = max(valores)
menor = min(valores)

for i in range(len(valores)):
    if valores[i] == maior:
        posicao_maior.append(i)

for i in range(len(valores)):
    if valores[i] == menor:
        posicao_menor.append(i)

print(posicao_maior)
print(posicao_menor)

print(f'O maior valor é o {maior} e está na ', end='')
for v in posicao_maior:
    print(f'{v+1}° posição...', end='')

print(f'\nO menor valor é o {menor} e está na ', end='')
for v in posicao_menor:
    print(f'{v+1}° posição... ', end='')
