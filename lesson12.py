# bosh_toplam = set()
# print(type(bosh_toplam))
#
# bosh_toplam.update({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
# print(bosh_toplam)
#
# bosh_toplam.remove(4)
# bosh_toplam.discard(6)
# print(bosh_toplam)
#
# toplam_1 = {1, 2, 3, 4, 5}
# toplam_2 = {4, 5, 6, 7, 8}
#
# birlashgan_toplam = toplam_1.union(toplam_2)
# print(birlashgan_toplam)
#
# umumiy_elementlar = toplam_1.intersection(toplam_2)
# print(umumiy_elementlar)
#
# farqi = toplam_1.difference(toplam_2)
# print(farqi)
#
# tekshirish = toplam_1 == toplam_2
# print(tekshirish)
#
tel_password = "12213"
answer = input('tel parolini kiriting>>>')

urinish = 1
while answer != tel_password:
    print('wrong answer')
    answer = input('tel parolini kiriting>>>')
    urinish += 1
    if urinish == 3:
        print("3 tdan ko'p urindingiz")
        break

# print(f'togri topdiz {urinish} ta urinishda topdiz')
