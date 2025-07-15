"""
Curso em video: Validando expressões

Lê uma expressão e verifica se os parênteses
estão abertos e fechados na ordem correta.
"""

expressao = input('Digite uma expressão: ')
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
