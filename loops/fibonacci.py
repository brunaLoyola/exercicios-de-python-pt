"""
Curso em Vídeo: Sequência de Fibonacci

Lê um número inteiro N e exibe os N primeiros
elementos da sequência de Fibonacci.
"""


numero = int(input('Digite um número: '))
t1 = 0
t2 = 1
cont = 3

print(f'{t1} -> {t2} ', end='')

while cont <= numero:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
