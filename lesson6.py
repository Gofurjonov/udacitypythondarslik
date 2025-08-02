# ozgaruvchi = [42, "hi", True, None, 10**20]
# turi = []
# for x in ozgaruvchi:
#     turi.append(type(x))
# print(turi)

# togri =  [0, 1, "", "ok", None, " ", [], 5]
# logikal = []
# for b in togri:
#     print(bool(b))
#     logikal.append(bool(b))
# print(logikal)
#
# prices = [12000, 34000, 8000, 15000]
# yigindi = 0
# for qoshish in prices:
#     yigindi =  yigindi + qoshish
# print("Umumiy summa: ", yigindi)
#
# scores = [56, 88, 92, 73, 92, 67]
# eng_katta = scores[0]
# for i in scores:
#     if i > eng_katta:
#         eng_katta = i
# print('Eng kattasi:', eng_katta)

# words = ["py", "loop", "array", "if"]
# box = []
# for word in words:
#     box.append(len(word))
# print(box)

nums=[3,4,9,12,15,18,19]
b=[]
c=[]
for i in nums:
    if i%2==0:
        b.append(i)
    elif i%2==1:
        c.append(i)
print(b)
print(c)