"""
Curso em video: Contador

Função contador() que realiza contagens com início, fim e passo.
Inclui contagem crescente, decrescente e personalizada.
"""
from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if inicio < fim:
        for num in range(inicio, fim+1, passo):
            print(f'{num} ', end='', flush=True)
            sleep(0.5)
        print('Fim')
    else:
        for num in range(inicio, fim+1, -passo):
            print(f'{num} ', end='', flush=True)
            sleep(0.5)
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem')
i = int(input('íncio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
