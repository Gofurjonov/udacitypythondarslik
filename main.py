# import lesson13modul
# avto1 = lesson13modul.avto_info("Gm", "Malibu", "Qora", "avtomat", 2025, 38000)
# lesson13modul.info_print(avto1)

# import lesson13modul as l13mod
# avto1 = l13mod.avto_info("Gm", "Malibu", "Qora", "avtomat", 2025, 38000)
# l13mod.info_print(avto1)

# from lesson13modul import avto_info, info_print
# avto1 = avto_info("Gm", "Malibu", "oq", "avtomat", 2025, 38000)
# info_print(avto1)

# from lesson13modul import avto_info as ainfo, info_print as iprint
# avto1 =ainfo("Gm", "Malibu", "Qora", "avtomat", 2025, 38000)
# iprint(avto1)

# from lesson13modul import *
# avto1 = avto_info("Gm", "Malibu", "Qora", "avtomat", 2025, 38000)
# info_print(avto1)

# import math
# x=81
# print(math.sqrt(x))
# print(math.pow(5,3))
# print(math.pi)
# print(math.log2(8))
# print(math.log10(100))

# import  random as r
# son = r.randint(0,100)
# print(son)

import random as r
ismlar = ["olim", "jamshid", "Mirzo", "shoxrux"]
ism = r.choice(ismlar)
print(ism)