"""
Curso em video: Informando características de uma variável

Receba uma entrada do usuário e exiba características
sobre o valor digitado:
    - Tipo primitivo
    - Se é numérico, alfabético ou alfanumérico
    - Presença de espaços
    - Formato de capitalização
    (minúsculas, maiúsculas ou capitalizado)
"""

variavel = input('Digite algo: ')

print('O tipo primitivo é: ', type(variavel))
print('O valor digitado é um número? ', variavel.isnumeric())
print('O valor digitado só tem espaços? ', variavel.isspace())
print('O valor digitado é alfabético?', variavel.isalpha())
print('O valor digitado é alfanumérico?', variavel.isalnum())
print('O valor digitado está em letras minusculas?', variavel.islower())
print('O valor digitado está em letras maiusculas?', variavel.isupper())
print('O valor digitado está captalizado?', variavel.istitle())
