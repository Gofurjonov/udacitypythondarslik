# balance = 1000
# while balance > 0:
#     try:
#         amount = int(input(f"Balansingiz: ${balance}. Qancha yechmoqchisiz? "))
#         if amount <= 0:
#             raise ValueError("Iltimos, musbat son kiriting!")
#         if amount > balance:
#             print("Yetarli mablag' yo'q!")
#         else:
#             balance -= amount
#             print(f"{amount}$ mablag' yechildi. Qolgan balans: {balance}$")
#         if balance == 0:
#             break
#     except ValueError:
#         print("Noto'g'ri kiritish! Faqat raqam kiriting.")
#         continue

# total = 0
# while True:
#     try:
#         item = input("Mahsulot narxini kiriting (yoki 'stop' deb yozing): ")
#         if item.lower() == "stop":
#             break
#
#         price = float(item)
#         if price <= 0:
#             raise ValueError("Narx musbat bo'lishi shart!")
#
#         total += price
#         print(f"{price} so'm qo'shildi. Jami: {total} so'm")
#     except ValueError:
#         print("Xato! Faqat to'g'ri narx kiriting (masalan: 15000 yoki 12500.50)")
#         continue

# maqsad = 10000
# yurgan_qadamlar = 0
# kunlar = 0
#
# while yurgan_qadamlar < maqsad:
#     try:
#         qadam = int(input(f"{kunlar + 1}-kun qadamlar sonini kiriting: "))
#         if qadam <= 0:
#             raise ValueError("Qadamlar soni 0 dan katta bo'lishi kerak!")
#
#         yurgan_qadamlar += qadam
#         kunlar += 1
#     except ValueError:
#         print("Noto'g'ri qiymat! Faqat butun son kiriting (masalan: 5000)")
#         continue
#
# print(f"Tabriklaymiz! {kunlar} kun ichida {yurgan_qadamlar} qadam yurib maqsadingizga erishdingiz!")

# while True:
#     try:
#         n = int(input("Nechta ishchi ish soati kiritasiz? "))
#         if n <= 0:
#             raise ValueError("Ishchilar soni 0 dan katta bo'lishi kerak!")
#         break
#     except ValueError:
#         print("Noto'g'ri kiritish! Faqat musbat butun son kiriting.")
#         continue
#
# i = 1
#
# while i <= n:
#     try:
#         hours = float(input(f"{i}-ishchining haftalik ish soatini kiriting: "))
#         if hours < 0:
#             raise ValueError("Ish soati manfiy bo'lishi mumkin emas!")
#
#         if hours < 40:
#             print(f"Ogohlantirish: {i}-ishchi {hours} soat ishlagan - 40 soatdan kam!")
#         else:
#             print(f"{i}-ishchi {hours} soat ishlagan - me'yorda")
#
#         i += 1
#
#     except ValueError as e:
#         print(f"Xato: {e}. Qaytadan kiriting.")
#         continue
#
# print("\nBarcha ishchilarni ish soatlari tekshirildi")

todo_list = []
print("Vazifalarni kiritish (tugatish uchun 'exit' deb yozing)")

while True:
    try:
        task = input("Yangi vazifani kiriting: ")
        if task.strip() == '':  # Bo'sh joy kiritilganini tekshirish
            raise ValueError("Vazifa bo'sh bo'lishi mumkin emas!")

        if task.lower() == 'exit':
            break

        todo_list.append(task)
        print(f"'{task}' ro'yxatga qo'shildi")

    except ValueError as e:
        print(f"Xato: {e}")
        continue

print("\nYakuniy vazifalar ro'yxati:")
for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")