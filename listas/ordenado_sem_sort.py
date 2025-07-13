"""
Curso em video: Ordenando sem sort

Recebe valores do usuário e os insere em ordem crescente
sem usar a função sort().
"""

valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        if len(valores) == 0 or valor > valores[-1]:
            valores.append(valor)
        else:
            pos = 0
            while pos < len(valores):
                if valor <= valores[pos]:
                    valores.insert(pos, valor)
                    break
                pos += 1

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print(f'Esta é sua lista ordenada: {valores}')
