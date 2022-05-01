'''
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
hipot = (cat_op ** 2 + cat_adj**2) ** (1/2)
print(f'O comprimento da  hipotenusa é {hipot:.2f}')
'''
'''
import math
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
hipot = math.hypot(cat_op, cat_adj)
print(f'O comprimento da  hipotenusa é {hipot:.2f}')
'''
from math import hypot
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
print(f'O comprimento da  hipotenusa é {hypot(cat_op, cat_adj):.2f}')
