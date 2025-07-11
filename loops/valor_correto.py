"""
Curso em Vídeo: Validação de sexo

Faça um programa que leia o sexo de uma pessoa,
aceitando apenas os valores 'M' ou 'F'.
Caso o valor esteja incorreto, solicite a digitação novamente
até receber um valor válido.
"""

valor = ''

while 'M' != valor != 'F':
    valor = input('Digite o seu sexo M ou F: ').upper()

print(f'O valor digitado foi {valor}')
