"""
Exercício:

Retorna nomes com mais de cinco letras em ordem alfabética.
"""

lista = []
cinco_letras = []

while True:
    nome = input('Digite um nome (digite "sair""): ').strip().lower()

    if nome == 'sair':
        break
    else:
        lista.append(nome)

for item in lista:
    if len(item) > 5:
        cinco_letras.append(item)

cinco_letras.sort()
print(f'Os nomes que possuem mais de cinco letras são: {cinco_letras}\n')
