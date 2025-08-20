from datetime import datetime

products = {
    "planshet": {"narxi": 1200, "soni": 20, "sana": '2025-02-03'},
    "notebooke": {"narxi": 800, "soni": 20, "sana": '2025-05-01'},
    "iphone 16": {"narxi": 1500, "soni": 20, "sana": '2025-03-05'}
}

admins = {
    "sara": {'login': 'sara123', 'parol': '12345'},
    "sardor": {'login': 'sardor111', 'parol': '12345'},
    "sarvar": {'login': 'sarvar122', 'parol': '12345'},
}


# def admin_cmd():
#     global admins
#     print("Iltimos shu yerga bizning admingiz bolsangiz parol va logingizni kiriting".title())
#     login=input("Logingizni kiriting!>>>")
#     password=input("Parolgizni kititing>>>")
#     for k,v in admins.items():
#         if login == v['login'] and password == v['parol']:
#             print(f" Xush kelibsiz {k.capitalize()}!")
#         else:
#             print()
# def kirim_chiqim():
#     global products
#     admin_call_data=input("Iltimos shu yerga toliq sanani kiriting (2025-03-05) qilib>>>")
#     for k,v in products.items():
#         if admin_call_data == v:
#             print(f"{k}")
#         else:
#             print("Bunqa sanada hech narsa bolamadi")
def hisobot():
    global products
    sana = input("Qaysi sanaga hisobot kerak? (masalan: 2025-03-05)> ")
    print(f"\n{sana} kunidagi mahsulotlar:")
    topildi = False
    for k, v in products.items():
        if v.get("sana") == sana:
            umumiy = v["narxi"] * v["soni"]
            print(f"{k.capitalize()} → narxi: {v['narxi']}$, soni: {v['soni']} dona, umumiy: {umumiy}$")
            topildi = True
    if not topildi:
        print("Bu sanaga mahsulot topilmadi")


def productlar():
    global products
    for k, v in products.items():
        umumiy = v["narxi"] * v["soni"]
        print(f"{k.capitalize()} → narxi: {v['narxi']}$, soni: {v['soni']} dona, umumiy: {umumiy}$")


def yangilash():
    global products
    hozir = datetime.now().strftime("%Y-%m-%d")
    for k, v in products.items():
        umumiy = v["narxi"] * v["soni"]
        print(f"{k.capitalize()} → narxi: {v['narxi']}$, soni: {v['soni']} dona, umumiy: {umumiy}$")
    kiritish_ad = input("Mahsulot nomini kiriting> ").lower()

    if kiritish_ad in products:
        soni = int(input(f"{kiritish_ad} qancha keldi (faqat son!!!)> "))
        narxi = int(input(f"{kiritish_ad} yangi narxi (hozirgi {products[kiritish_ad]['narxi']}$)> "))

        products[kiritish_ad].update({
            "narxi": narxi,
            "soni": products[kiritish_ad]["soni"] + soni,
            "sana": hozir
        })
        print(f"{kiritish_ad.capitalize()} yangilandi: {products[kiritish_ad]}")
    else:
        narxi = int(input("Yangi mahsulot narxi> "))
        soni = int(input("Yangi mahsulot soni> "))
        products.update({
            kiritish_ad: {"narxi": narxi, "soni": soni, 'sana': hozir}
        })
        print(f"{kiritish_ad.capitalize()} qo‘shildi: {products[kiritish_ad]}")


def chiqarish():
    price = 0
    global products
    for k, v in products.items():
        umumiy = v["narxi"] * v["soni"]
        print(f"{k.capitalize()} → narxi: {v['narxi']}$, soni: {v['soni']} dona, umumiy: {umumiy}$")
    nomi = input("Shulardan qanaqa product olmoqchisiz>".lower())
    if nomi in products:
        soni = int(input("Qancha olmoqchisiz>"))
        price = products[nomi]['narxi'] * soni
        products[nomi]["soni"] -= soni
        print(f"{soni} ta {nomi} oldingiz. Qolgan soni: {products[nomi]['soni']} dona.")
        print("Umumiy narx:", price, "$")
    else:
        pass


# def main():
#     while True:
#         try:
#             kiriysh = int(
#                 input("(1).kiritish | (2).chiqarish | (3).productlar | (4).hisobot | (5).help | (0).chiqish >>> "))
#         except ValueError:
#             print("❌ Faqat 1, 2, 3, 4, 5 yoki 0 ni ishlata olasiz")
#             continue  # noto'g'ri kiritilganda sikl qaytadan boshlansin
#
#
#
#         if kiriysh == 1:
#             yangilash()
#         elif kiriysh == 2:
#             chiqarish()
#         elif kiriysh == 3:
#             productlar()
#         elif kiriysh == 4:
#             hisobot()
#         elif kiriysh == 5:
#             print("1 → Omborga mahsulot kiritish\n"
#                   "2 → Ombordan chiqarish (sotish)\n"
#                   "3 → Hamma mahsulotni ko‘rish\n"
#                   "4 → Sana bo‘yicha hisobot\n"
#                   "0 → Dasturdan chiqish")
#         elif kiriysh == 0:
#             print("✅ Code to‘xtadi")
#             break
#         else:
#             print("❌ Faqat 1, 2, 3, 4, 5 yoki 0 ni tanlang")
# if __name__ == '__main__':
#     main()
