# lambda YOHUD NOMSIZ FUNKSIYA
# import math
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))
#
# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))

# def daraja(n):
#     return lambda x : x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga,"
#       f"kubi {kub(3)} ga teng")

from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)

# def daraja2(x):
#     return x*x
# print(list(map(daraja2, sonlar)))

# kvadrat = list(map(lambda x: x*x, sonlar))
# print(kvadrat)

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x, y: x+y, a, b))
# print(a_plus_b)

import random as r
# sonlar = r.sample(range(100), 10)
# # print(sonlar)
# def juftmi(x):
#     return x%2==0
# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)

# juft_sonlar = list(filter(lambda son: son%2 == 0, sonlar))
# print(juft_sonlar)

# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
#
# mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
# print(mevalar_b)