"""
Objetivo:
    Solicitar números ao usuário e somá-los até que ele digite zero.

Etapas:
    1. Solicitar números em um loop;
    2. Somar os valores digitados;
    3. Encerrar quando o número zero for digitado;
    4. Exibir a soma total.
"""

soma = 0
numero_usuario = 1

while numero_usuario != 0:
    numero_usuario = int(input('Digite o número a ser somado (0 para sair): '))
    soma += numero_usuario

print('Total: ', soma)
