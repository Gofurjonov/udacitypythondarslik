#task 1,1 if
# a)
# harorat = int(input("Haroratni kiriting (C): "))
#
# if harorat < 0:
#     print("Sovuq kun, issiqroq kiying!")
# elif 0 <= harorat <= 20:
#     print("Ob-havo yaxshi, lekin sal sovuq.")
# else:
#     print("Juda yaxshi ob-havo, zavqlaning!")

#task2
# #b)
# yoshi = int(input("Futbolchining yoshi: "))
# gollari = int(input("Urgan gollari soni: "))
#
# if yoshi < 18:
#     if gollari >= 1:
#         print("Yosh iste'dod")
#     else:
#         print("Mashq qilish kerak!")
# elif 18 <= yoshi <= 35:
#     if gollari >=3:
#         print("Yulduz futbolchi")
#     else:
#         print("Oddiy futbolchi! ")
# elif yoshi > 35:
#     if gollari >= 1:
#         print("Mag'lubiyatsiz veteran! ")
#     else:
#         print("Tajribali murabbiy.")

# task 1,2 for
# sonlar = [1, 2, 7, 10, 8]
# eng_kattasi = sonlar[0]
# for son in sonlar:
#     if son > eng_kattasi:    #eng kattasi
#         eng_kattasi = son
# print(eng_kattasi)

# sonlar = [1, 2, 7, 10, 8]
# eng_kichik = sonlar[0]
# for son in sonlar:
#     if son < eng_kichik:    #eng kichigi
#         eng_kichik = son
# print(eng_kichik)

# sonlar = [1, 2, 7, 10, 8]
# yigindi = 0
# for son in sonlar:    #yigindi
#     yigindi += son
# print(yigindi)

# sonlar = [1, 2, 7, 10, 8]
# kopaytma = 1
#
# for son in sonlar:
#     kopaytma *= son
#                                 #kopaymat
# print("Ko'paytma:", kopaytma)

# for i in range(1, 10):  # 1 dan 9 gacha
#     for j in range(1, 10):  # 1 dan 9 gacha
#         print(f"{i} x {j} = {i*j}")
#     print()  # Qatorni tashlash

import random

# Kompyuter 1-20 oralig'ida tasodifiy son tanlaydi
import random

# Kompyuter 1 dan 20 gacha son o‘ylaydi
sirli_son = random.randint(1, 20)

# Foydalanuvchi taxminlari soni
urinishlar = 0

print("Men 1 dan 20 gacha bir son o‘yladim. Topishga harakat qiling!")

while True:
    taxmin = int(input("Son kiriting: "))
    urinishlar += 1

    if taxmin < sirli_son:
        print("Yuqoriroq son kiriting.")
    elif taxmin > sirli_son:
        print("Pastroq son kiriting.")
    else:
        print(f"Tabriklaymiz! To‘g‘ri topdingiz. Urinishlar soni: {urinishlar}")
        break
