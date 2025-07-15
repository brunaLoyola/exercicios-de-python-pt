"""
Exercício:

Realiza operações com listas, incluindo união, repetição,
funções integradas e métodos de modificação.
"""

lista_01 = [1, 2, 3, 4]
lista_02 = [5, 6, 7, 8]

uniao = lista_01 + lista_02
print(uniao)

repeticao = uniao * 2
print(repeticao)

print(f'O maior número da lista é {max(uniao)}')
print(f'O menor número da lista é {min(uniao)}')
print(f'A soma de todos os números da lista {sum(uniao)}')
print(f'Lista ordenada: {sorted(uniao)}')
print(f'Lista invertida: {list(reversed(uniao))}')

uniao.append(5)
print(uniao)

uniao.insert(3, 6)
print(uniao)

uniao.remove(2)
print(uniao)

uniao.pop(1)
print(uniao)

print(uniao.count(6))

print(uniao.index(8))

copia = uniao.copy()
copia.append(4)

print(f'Lista original: {uniao}')
print(f'Cópia: {copia}')

uniao.extend(copia)
print(uniao)
