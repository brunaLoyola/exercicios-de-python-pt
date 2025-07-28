"""
Curso em video: Módulo de funções

Crie um módulo chamado moeda.py que tenha
as funções aumentar(), diminuir(), dobro() e metade().
Depois, crie um programa que importe esse módulo e use algumas dessas funções.
"""

from funcoes_moeda import resumo

valor = float(input('Digite o preço: R$ '))

resumo(valor, 20, 12)
