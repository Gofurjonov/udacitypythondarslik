# a) "ismlar" => bosh ro'yxat va unga elementlar qo'shamiz
ismlar = []  # Bo‘sh ro‘yxat
ismlar.append("Alisher")
ismlar.append("Asadbek")
ismlar.append("Dilmurod")
ismlar.append("Zafar")
ismlar.append("Samir")

print("Ismlar:", ismlar)

# b) Elementlarni o'zgartiramiz
ismlar[1] = "Hasan"  # 2-element (Vali) o‘rniga Hasan
print("O'zgargan ismlar:", ismlar)

# c) Elementlarni o‘chirish
ismlar.pop(2)
del ismlar[0]
ismlar.remove("Zafar")
print("Tozalangan ismlar:", ismlar)
# Izoh:
# - pop(index): belgili indeksdagi elementni o‘chiradi va uni qaytaradi
# - del list[index]: shunchaki o‘chiradi, lekin qaytarmaydi
# - remove(value): birinchi uchragan qiymatni o‘chiradi, indeks kerak emas

# d) "yaqinlar" listiga nusxa olish
yaqinlar = ismlar.copy()
# yaqinlar = ismlar[:] ikkinchi usuli

# e) "yaqinlar"ni alifbo tartibida tartiblaymiz
yaqinlar.sort()

print("Yaqinlar (tartiblangan):", yaqinlar)
print("Ismlar (asl):", ismlar)

# f) 1 dan 100 gacha bo‘lgan list (teskari tartibda)
sonlar = list(range(1, 101))
sonlar.reverse()  # Teskari qiladi
print("Teskari sonlar:", sonlar)
boshidan = sonlar[:10]
ortasidan = sonlar[45:55]
oxiridan = sonlar[-10:]

yangi_list = boshidan + ortasidan + oxiridan
print("Yangi ro'yxat: ", yangi_list)


number = tuple(range(1,11))
print("Tuple sonlar: ", number)
print("4 da 7 gacha: ", number[3:7])

number_list = list(number)
number_list[0] = 27
number = tuple(number_list)
print("O'zgartirilgan tuple: ",number)