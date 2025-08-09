# ismlar = []
# odamlar = {}
#
# while True:
#     ism = input("Ismingizni kiriting: ")
#     yosh = int(input(f"{ism} ning yoshini kiriting: "))
#     ismlar.append(ism)
#     odamlar[ism] = yosh
#     javob = input("yana dos'tingizni kiritasizmi? (ha/yoq): ")
#     if javob.lower() == "yoq":
#         break
# print("Kiritgan do'stlaringizni ro'yhati:", ismlar)
#
# print("Do'stlaringiz va ularning yoshlari: ")
# for ism, yosh in odamlar.items():
#     print(f"{ism} : {yosh} yosh")

# balance = 1000
# while balance > 0:
#     amount = int(input(f"Balansingiz: ${balance}. Qancha yechmoqchisiz? "))
#     if amount > balance:
#         print("Yetarli mablag' yoq")
#     else:
#         balance -= amount
#         print(f"{amount} mablag' yechildi. Qolgan balans: {balance}")
#     if balance == 0:
#         break

# total = 0
# while True:
#     item = input("Mahsulot narxini kiriting yoki 'stop' deb yozing: ")
#     if item.lower() == "stop":
#         break
#
#     price = float(item)
#     total += price
#     print(f"{price} so'm qo'shildi. Jami: {total} so'm")

# goal = 10000
# yurgan_qadamlar = 0
# kunlar = 0
#
# while yurgan_qadamlar < goal:
#     qadam = int(input(f"{kunlar + 1}-kun qadamlar sonini kiriting: "))
#     yurgan_qadamlar += qadam
#     kunlar +=1
# print(f"Maqsadga {kunlar} kunda erishildi! jami {yurgan_qadamlar} qadam yurdingiz")

# month = 1
# paid_months = 0
# while month <= 12:
#     status = input(f"{month}-oy ijarani to‘ladingizmi? (ha/yo‘q): ")
#     if status.lower() == "ha":
#         paid_months +=1
#     month +=1
#
# print(f"Siz {paid_months} oy ijarani to‘ladingiz.")

# task 7
# todo_list = []
# print("Vazifalarni kiritish (tugatish uchun 'exit' deb yozing)")
#
# while True:
#     task = input("Yangi vazifani kiriting: ")
#     if task.lower() == 'exit':
#         break
#     todo_list.append(task)
#     print(f"'{task}' ro'yxatga qo'shildi")

# task 6
n = int(input("Nechta ishchi ish soati kiritasiz? "))
i = 1

while i <= n:
    hours = float(input(f"{i}-ishchining haftalik ish soatini kiriting: "))
    if hours < 40:
        print(f"Ogohlantirish: {i}-ishchi {hours} soat ishlagan - 40 soatdan kam!")
    else:
        print(f"{i}-ishchi {hours} soat ishlagan - me'yorda")
    i += 1

print("Barcha ishchilarni ish soatlari tekshirildi")