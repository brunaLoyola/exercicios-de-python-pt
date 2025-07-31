"""
Curso em Vídeo - Verificando Acessibilidade de Site

Este script testa se o site 'http://www.pudim.com.br' está acessível
a partir do computador local,
utilizando tratamento de exceções com urllib.
"""

from urllib import request, error

try:
    site = request.urlopen('http://www.pudim.com.br')
except error.URLError:
    print('O site pudim não está acessível no momento!')
else:
    print('Consegui acessar o site pudim com sucesso!')
