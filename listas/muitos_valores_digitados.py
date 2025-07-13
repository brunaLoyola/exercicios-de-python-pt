"""
Curso em video: Números e informações

Lê vários números em uma lista e exibe quantidade digitada,
valores em ordem decrescente e se o número 5 está presente.
"""

valores = []

while True:
    valor = int(input('Digite um valor: '))
    continuar = input('Deseja continuar [S/N]: ').upper()

    if continuar in 'N':
        valores.append(valor)
        break
    else:
        valores.append(valor)

lista_ordenada = sorted(valores, reverse=True)
print(f'Foram digitados {len(valores)} números')
print(f'Essa é a lista em forma decrescente: {lista_ordenada}')

if 5 in valores:
    print(f'O número 5 está na lista, na {valores.index(5)+1}° posição')
else:
    print('O número 5 não está na lista')
