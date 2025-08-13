# funksiyalar

# name = 'Ali'
# print('salom',name)
#
# name = 'Vali'
# print('salom',name)
#
# name = 'Gani'
# print('salom',name)

# def salom_ber(name):
#     """
#
#     :param name:
#     :return:
#     """
#     print('salom',name)

# salom_ber(name='Ali')
# salom_ber(name='Vali')
# salom_ber(name='Gani')
# salom_ber('Feruz')

# darajani hisoblash funksiyasi

# def daraja(a=2,b=3):
#     print(f'{a}^{b}={a**b}')
#     return a**b

# daraja(2,4)
# daraja(b=4,a=2)
# a = daraja(3,4) # 3^4=81
# print(a) # 81

# def yasa_full_name(ism,familya,sharif):
#     return f'{ism} {familya} {sharif}'
#
# full_name = yasa_full_name('Ali','Valiyev','Gani ogli')
# print(full_name)  #'Ali','Valiyev','Gani ogili

# def summa(*args,**kwargs):
#     total = 0
#     for i in args:
#         total += i
#
#     for v in kwargs.values():
#         total+=v
#
#     return total
#
#
# print(summa(12,12,34,56,76,4,a=12,b=21,c=32))

# global va local ozgaruvchilar

# x = 10
#
#
# def change_x():
#     global x
#     x = 20
#     print(x)  # 20
#     return x
#
# change_x()
# print(x) # 10
