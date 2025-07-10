"""
Curso em vídeo: Adivinhando o número

Gera um número aleatório entre 0 e 5 e verifica se o usuário acertou a escolha.
"""

from random import randint

numero = randint(0, 5)
numero_usuario = int(input('Adivinhe um número entre 0 e 5: '))

if numero == numero_usuario:
    print(f'O número {numero} é o correto. Parabéns!!')
else:
    print(f'O número correto é {numero}. Tente na próxima!!')
