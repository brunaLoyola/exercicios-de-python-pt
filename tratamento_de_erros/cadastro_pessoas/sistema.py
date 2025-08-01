"""
Curso em Vídeo: Sistema de Cadastro

Apresenta um menu interativo com três opções:
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema

O programa utiliza módulos separados para interface e manipulação de arquivos,
com tratamento de exceções para entradas inválidas.

Ao iniciar, o sistema verifica se o arquivo de cadastro existe.
Se não existir, cria automaticamente um arquivo .txt para armazenar os dados.
"""

from lib.arquivo import arquivo_existe, criar_arquivo, ler_arquivo
from lib.interface import menu, cabecalho
from time import sleep

arq = 'bruna.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(
        ['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema']
    )
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 02')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo')
        break
    else:
        print('Erro!! Digite uma opção válida')
    sleep(2)
