# # filelar text
#
# # oddiy fileni oqish
# # file = open('pi.txt')
# # a = file.read()
# # print(a)
# # file.close()
#
#
# # with open('pi2.txt') as f:  # context manager
# #     a = f.read()
# #     print(a)
#
# # kop qatorli oqish
# # with open('pi.txt') as f:  # context manager
# #     for i in f:
# #         print(i.strip())
#
# # print('file yopildi')
# # try:
# #     with open('pi2.txt') as f:  # context manager
# #         for i in f:
# #             print(i.strip())
# # except FileNotFoundError as e:
# #     print(e)
#
#
# # with open('pi2.txt','w') as f:
# #     f.write('sadsadsd')
#
# # with open('pi2.txt','a') as f:
# #     f.write('\nsalom1')
#
# #                   r+w
# # with open('pi2.txt',"r+") as f:
# #     print(f.read())
# #     f.seek(3)
# #     f.write('salom')
#
# # with open('pi.txt',"w+") as f:
# #     # f.seek(0)
# #     f.write('salom')
# #     f.seek(0)
# #     print(f.read())
#
# # pickle
# #
# # talaba = {
# #     "ism":"ali",
# #     "yoshi":21
# # }
# #
# # class A:
# #     def __init__(self,name):
# #         self.name = name
# #
# # a = A('ali')
# #
# # import pickle
# #
# # with open('data.dat',"wb") as f:
# #     pickle.dump(a,f)
# #
# #
# # with open('data.dat','rb') as f:
# #     a = pickle.load(f)
# #     print(a.name)
# #     print(type(a))
#
#
# # json
#
# import json
#
# data = {
#     'name': "ali",
#     "age": 21
# }
#
# # with open('data.json', 'w') as f:
# #     json.dump(data,f)
#
#
# with open('data.json','r') as f:
#     a = json.load(f)
#     print(a)

# sonlar = [1, 4, 7, 10]
# yigindi = 0
# for i in sonlar:
#     yigindi += i
#
# print("Yig'indi:", yigindi)

import csv

# CSV faylini yozish
with open('person.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['age', 'name', 'surname'])
    writer.writerow([21, 'Ali', 'Valiyev'])
    writer.writerow([25, 'Alish', 'Valiyev'])
    writer.writerow([32, 'Aliya', 'Valiyev'])

# CSV faylini o'qish va yoshlar yig'indisini hisoblash
with open('person.csv', 'r', newline="") as f:
    reader = csv.reader(f)
    yosh_yigindisi = 0

    for index, row in enumerate(reader):
        if index == 0:  # Sarlavha qatorini o'tkazib yuborish
            continue
        try:
            yosh = int(row[0])  # Birinchi ustundagi yoshni songa aylantirish
            yosh_yigindisi += yosh
            print(f"{row[1]} {row[2]}: {yosh} yosh")
        except (ValueError, IndexError):
            print(f"Xato: {row} qatorida yosh maydoni noto'g'ri")

print(f"\nYoshlar yig'indisi: {yosh_yigindisi}")