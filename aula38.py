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
import random

primeiros_digitos = ''
for digito in range(9):
    primeiros_digitos += str(random.randint(0, 9))

multiplicador_1 = 10

total_1 = 0
for digito in primeiros_digitos:
    total_1 += int(digito) * multiplicador_1
    multiplicador_1 -= 1

digito_1 = (total_1 * 10) % 11   
digito_1 = digito_1 if digito_1 <= 9 else 0

primeiros_digitos += str(digito_1)
multiplicador_2 = 11
total_2 = 0

for digito in primeiros_digitos:
    total_2 += int(digito) * multiplicador_2
    multiplicador_2 -= 1

digito_2 = (total_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


resultado = primeiros_digitos + str(digito_2)
print(resultado)
