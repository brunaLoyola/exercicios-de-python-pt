"""
Curso em video: Sistema de Cadastro

Apresenta um menu interativo com três opções:
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema

O programa utiliza módulos separados para interface,
com tratamento de exceções para entradas inválidas.
"""

from lib.interface import menu, cabecalho
from time import sleep

while True:
    resposta = menu(
        ['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema']
    )
    if resposta == 1:
        cabecalho('Opção 01')
    elif resposta == 2:
        cabecalho('Opção 02')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo')
        break
    else:
        print('Erro!! Digite uma opção válida')
    sleep(2)
