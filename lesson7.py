#task 7
# nums = [10,20,30,40]
# target = 30
# for i in range(len(nums)):
#     if nums[i] == target:
#         print("Indeksi", i)
#         break

# task 8
# n = 5
# boxs = []
# for i in range(5):
#     boxs.append(i+1)
# print(boxs)

#task 9
# letters = ["a", "b", "c", "d"]
# revers_box = []
# for i in reversed(letters):
#     revers_box.append(i)
# print(revers_box)

#task10
# mevalar = ["olma", "banan", "anjir", "gilos"]
# harflar = []
#
# for i in mevalar:
#     if len(i) ==5:
#         harflar.append(i)
# print(harflar)


#task 12
# prices = [100000, 50000, 20000]
# boxs = []
# for i in prices:
#     yangi_narx = i * 0.85
#     boxs.append(int(yangi_narx))
# print(boxs)

#task 14
# stops = [(5, 2), (3, 1), (0, 4)]
# yolovchilar = 0
#
# for kirgan, chiqqan in stops:
#     yolovchilar -= chiqqan
#     yolovchilar += kirgan
#
# print("Oxirida yo‘lovchi:", yolovchilar)

#task 15
# cal = [450, 600, 300, 800]
# jami = sum(cal)
# if jami > 2500:
#     print("Limit oshdi")
# else:
#     print("yaxshi hammasi joyida")
# print("jami: ", jami)

#task 16
# rates = [12600, 12620, 12580, 12650]
# ortacha = sum(rates) / len(rates)
# print("O'rtacha kurs: ", ortacha)

#task 17
# matn = "salom dunyo salom"
# sozlar = matn.split()  # Matnni so‘zlarga bo‘lamiz
# soni = 0
#
# for soz in sozlar:
#     if soz == "salom":
#         soni += 1
#
# print('"salom" so‘zi soni:', soni)
