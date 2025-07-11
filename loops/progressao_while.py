"""
Curso em Vídeo: Progressão Aritmética com extensão

Lê os termos de uma progressão aritmética e permite ao usuário
solicitar mais termos até digitar 0 para encerrar.
"""


contador = 1
numero = int(input('Digite o primeiro termo de uma progressão aritmética: '))
razao = int(input('Informe a razão: '))
termo = numero

while contador <= 10:
    print(f'{termo}  ', end='')
    termo += razao
    contador += 1

print('FIM')
