'''
import math
ang = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(ang))
print(f' O ângulo de {ang}º, tem o SENO de {seno:.2f}')
coss = math.cos(math.radians(ang))
print(f' O ângulo de {ang}º, tem o COSSENO de {coss:.2f}')
tang = math.tan(math.radians(ang))
print(f'O ângulo de {ang}º, tem a TANGENTE de {tang:.2f}')
'''

from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer: '))
sen = sin(radians(ang))
print(f'O ângulo de {ang}º, possui SENO de {sen:.2f}')
cos = cos(radians(ang))
print(f'O ângulo de {ang}º, possui COSSENO de {cos:.2f}')
tang = tan(radians(ang))
print(f'O ângulo de {ang}º, possui TANGENTE de {tang:.2f}')