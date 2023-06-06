# Leia um angulo qualquer e mostre o valor do Seno, Cosseno e Tangente.

# https://docs.python.org/3/library/cmath.html#trigonometric-functions

import math

x = float(input('Digite o valor de um angulo '))


print('O Angulo de {} SENO é de {}'.format(x, math.sin(math.radians(x))))
print('O Angulo de {} COSSENO é de {}'.format(x, math.cos(math.radians(x))))
print('O Angulo de {} TANGENTE é de {}'.format(x, math.tan(math.radians(x))))