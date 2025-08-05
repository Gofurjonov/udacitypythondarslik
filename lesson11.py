# a)
# talaba_baholari = {
#     "Ali" : {"Matematika" : 5, "Ingliz tili": 4},
#     "Vali" : {"Matematika" : 4, "Ingliz tili": 3},
#     "Gani" : {"Matematika" : 2, "Ingliz tili": 3}
# }
# print(talaba_baholari)

# b)
# talaba_baholari.update({"Olim" : {"Matematika": 3, "Ingliz tili" : 4}})
# print(talaba_baholari)
#
# # c)
# del talaba_baholari["Vali"]
# print(talaba_baholari)

# del - indeks orqali o‘chiradi, qiymat qaytarmaydi.
# pop() - indeks orqali o‘chiradi va qiymat qaytaradi.

# d)
# for i, k in talaba_baholari.items():
#     print(f"{i} ning baholari: {k["Matematika"]}, {k["Ingliz tili"]}")
# # e)
# talaba_baholari["Ali"]["Matematika"] = 3
# print(talaba_baholari)

# f)
talaba_baholari = {
    "Ali" : {"Matematika" : 5, "Ingliz tili": 4},
    "Vali" : {"Matematika" : 4, "Ingliz tili": 3},
    "Gani" : {"Matematika" : 2, "Ingliz tili": 3}
}
# f) O'rtacha baholar lug'atini yaratamiz
ortalama_baholar = {}

for talaba, fanlar in talaba_baholari.items():
    baholar = list(fanlar.values())
    ortalama = sum(baholar) / len(baholar)
    ortalama_baholar[talaba] = ortalama

# g) O'rtacha bahosi 3 dan kichik bo'lgan talabalarni tekshiramiz
for talaba, ortalama in ortalama_baholar.items():
    if ortalama < 3:
        print(f"{talaba}, siz yiqildingiz! (O'rtacha baho: {ortalama})")