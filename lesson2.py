# # 1. <"O'zbekiston Vatan"im meni!!!> so'zini console'ga chiqaramiz
# print("<O'zbekiston Vatanim meni!!!>")
# # 2. Tezlik va masofani clientdan soraymiz(input operatori orqali) shu masofani mashina qancha
# # vaqtda bosib otishini topamiz(t = masofa/tezlik). f-string orqali malumotlarni <print> qilamiz.
#
# masofa = float(input("Masofani kiriting (km): "))
# tezlik = float(input("Tezlikni kiriting (km/s): "))
# vaqt = masofa / tezlik
# print(f"Vaqt: {vaqt} soat")
#
# #3.Har bir dasturimizga commit(izoh) yozamiz
# 
# # 4. code ni togirlaymiz.
# print("Notes from Day 1")
# print("The print statement is used to output strings")
# print("Strings are strings of characters")
# print("String Concatenation is done with the + sign")
# print("New lines can be created with a \\ and the letter n")
#
# #5.Float ma’lumot turidagi ikkita o’zgaruvchi bor a, b . b ni print qilsak a qiymatni, a ni print
# # qilsak b qiymatni chiqarishi kerak.
# a = 21
# b = 18
# a,b = b,a
# print(a)
# print(b)
#
# #task 6
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil.title())
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())
#
# # task 7
# # Qo'shish (+)
# print(5 + 3)  # 8
#
# # Ayirish (-)
# print(5 - 3)  # 2
#
# # Ko'paytirish (*)
# print(5 * 3)  # 15
#
# # Bo'lish (/)
# print(5 / 3)  # 1.666...
#
# # Butun qismli bo'lish (//)
# print(5 // 3)  # 1
#
# # Qoldiqli bo'lish (%)
# print(5 % 3)  # 2
#
# # Darajaga oshirish (**)
# print(5 ** 3)  # 125