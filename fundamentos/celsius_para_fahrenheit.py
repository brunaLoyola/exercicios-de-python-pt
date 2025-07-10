"""
Curso em video: Exercício de conversão de Celsius para Fahrenheit

Este módulo lê uma temperatura em graus Celsius fornecida pelo usuário,
converte-a para graus Fahrenheit usando a fórmula:

    °F = (°C x 1.8) + 32

apresentando ao final o resultado formatado na tela.
"""

temperatura = float(input('Digite a temperatura em °C: '))
conversao = (temperatura * 1.8) + 32

print(f'A temperatura de {temperatura}°C corresponde a {conversao}°F.')
