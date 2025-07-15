"""
Curso em video: Número por extenso

Lê um número entre 0 e 20 e o exibe por extenso usando uma tupla.
"""


nome_extenso = (
                'zero', 'um', 'dois', 'tres', 'quatro',
                'cinco', 'seis', 'sete', 'oito', 'nove',
                'dez', 'onze', 'doze', 'treze', 'catorze',
                'quinze', 'dezesseis', 'dezessete', 'dezoito',
                'dezenove', 'vinte'
            )

numero = int(input('Digite um número de 0 a 20: '))

print(f'O número é {nome_extenso[numero]}')
