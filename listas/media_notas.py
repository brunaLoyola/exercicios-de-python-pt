"""
Exercício:

Calcula a média de quatro notas e informa o status do aluno,
mostrando também a maior e a menor nota.
"""

lista_numeros = []
for numero in range(1, 5):
    lista_numeros.append(int(input(f'Digite sua {numero}° nota:')))

media = sum(lista_numeros) / 4

if media >= 7 and media <= 10:
    print('Você foi aprovado!')
elif media <= 7 and media >= 5:
    print('Você está de recuperação')
elif media > 10 or media < 0:
    print('Nota informada inválida')
else:
    print('Reprovado!')

print(
    f'A sua maior nota é: {max(lista_numeros)} \n'
    f'A sua menor nota é: {min(lista_numeros)}'
)
