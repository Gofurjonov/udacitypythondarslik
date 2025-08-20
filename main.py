from lesson19.task import yangilash,chiqarish,productlar,hisobot


def main():
    while True:
        try:
            kiriysh = int(
                input("(1).kiritish | (2).chiqarish | (3).productlar | (4).hisobot | (5).help | (0).chiqish >>> "))
        except ValueError:
            print("❌ Faqat 1, 2, 3, 4, 5 yoki 0 ni ishlata olasiz")
            continue  # noto'g'ri kiritilganda sikl qaytadan boshlansin



        if kiriysh == 1:
            yangilash()
        elif kiriysh == 2:
            chiqarish()
        elif kiriysh == 3:
            productlar()
        elif kiriysh == 4:
            hisobot()
        elif kiriysh == 5:
            print("1 → Omborga mahsulot kiritish\n"
                  "2 → Ombordan chiqarish (sotish)\n"
                  "3 → Hamma mahsulotni ko‘rish\n"
                  "4 → Sana bo‘yicha hisobot\n"
                  "0 → Dasturdan chiqish")
        elif kiriysh == 0:
            print("✅ Code to‘xtadi")
            break
        else:
            print("❌ Faqat 1, 2, 3, 4, 5 yoki 0 ni tanlang")

if __name__ == '__main__':
    main()