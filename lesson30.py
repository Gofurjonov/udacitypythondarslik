# file = open('pi')
# a = file.read()
# print(a)
# file.close()
from lesson19.modules import yigindi

# with open('pi') as f:
#     a = f.readlines()
#     print(a)
#
# new_lines = []
# for line in a:
#     if "-" in line:
#         name, grade = line.split("-")
#         grade = int(grade.strip())
#         if grade < 80:
#             grade += 5
#         new_lines.append(f"{name.strip()} - {grade} \n")
#     else:
#         new_lines.append(line)
#
# with open("pi","w") as f:
#     f.writelines(new_lines)
# print("Malumotlar yangilandi!")

# talabalar = []
#
# with open("pi.txt", "r") as file:
#     for i in file:
#         print(i.strip())
#         talabalar.append(i.strip().split(' - '))
#
# for i in talabalar:
#     if int(i[1]) < 80:
#         i[1] = int(i[1]) + 5
#
# with open('pi.txt', 'w') as file:
#     for i in talabalar:
#         file.write(f'{i[0]} - {i[1]}\n')

# nums = [1, 2, 3, 4]
#
#
# def running_sum(nums):
#     natija = []
#     jami = 0
#     for son in nums:
#         jami += son
#         natija.append(jami)
#     return natija

sonlar = [1, 4, 7, 10]
yigindi = 0
for i in sonlar:
    yigindi += i

print("Yig'indi:", yigindi)