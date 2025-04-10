'''
Exercício: validar um CPF

Cálculo do primeiro dígito do CPF:
CPF: 746.824.890-70
Multiplique os 9 primeiros dígitos do CPF por uma contagem
regressiva começando de 10 e depois some os resultados.

Ex:  746.824.890-70
    10  9  8  7  6  5  4  3  2
 *  7   4  6  8  2  4  8  9  0
    70 36  48 56 12 20 32 27 0

    Soma dos resultados = 301

Multiplique o resultado por 10 e obtenha o resta da divisão 
do número resultando por 11.

    301 * 10 = 3010
    3010 % 11 = 7

Se o resultado for maior que 9:
    O resultado é 0

Caso o contrário:
    O resultado permanece o mesmo.

O primeiro número do CPF é 7
'''
# Gerador simples de CPF válido:

import random
def calculo_digitos(base, multi):
    total = 0
    for digito in base:
        total += int(digito) * multi
        multi -= 1

    digito_final = (total * 10) % 11   
    digito_final = digito_final if digito_final <= 9 else 0

    base += str(digito_final)
    return base

cpf = ''
for digito in range(9):
    cpf += str(random.randint(0, 9))

cpf = calculo_digitos(cpf, 10)
cpf = calculo_digitos(cpf, 11)

print(cpf)
