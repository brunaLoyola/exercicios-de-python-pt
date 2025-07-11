"""
Curso em Vídeo: Soma de múltiplos de três

Calcula a soma de todos os números ímpares
múltiplos de três no intervalo de 1 até 500.
"""

soma = 0
cont = 0
for c in range(1, 501, +2):
    if c % 3 == 0:
        soma += c
        cont += 1

print(f'A soma total é de {soma}')
print(cont)
