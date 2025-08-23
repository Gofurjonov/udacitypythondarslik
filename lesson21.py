products = {
    'adrenaline': {'narxi': 200, 'soni': 20},
    'coca-cola': {'narxi': 10000, 'soni': 30},
    'morojniy': {'narxi': 20000, 'soni': 10},
    'non': {'narxi': 5000, 'soni': 200}
}


def display_menu():
    print(" OMBORXONA MENYUSI")
    print("1. Mahsulot qo'shish")
    print("2. Mahsulot olib chiqish")
    print("3. Mahsulotlar ro'yxati")
    print("4. Chiqish")
    print("=========================")


def add_product():
    try:
        nom = input("Mahsulot nomi: ").strip().lower()
        if not nom:
            print("Nom kiritish shart!")
            return

        narxi = int(input("Narxi: "))
        soni = int(input("Soni: "))

        if narxi <= 0 or soni <= 0:
            print("Son kiriting (0 dan katta)")
            return

        if nom in products:
            products[nom]['soni'] += soni
            print(f"OK. {nom} mahsulotining yangi soni: {products[nom]['soni']}")
        else:
            products[nom] = {'narxi': narxi, 'soni': soni}
            print(f"OK. {nom} yangi mahsulot qo'shildi")

    except ValueError:
        print("Son kiriting (0 dan katta)")


def remove_product():
    try:
        nom = input("Mahsulot nomi: ").strip().lower()
        if not nom:
            print("Nom kiritish shart!")
            return

        if nom not in products:
            print("Mahsulot topilmadi")
            return

        miqdor = int(input("Olib tashlash miqdori: "))
        if miqdor <= 0:
            print("Son kiriting (0 dan katta)")
            return

        available = products[nom]['soni']
        if available < miqdor:
            print(f"Mayjud: {available} dona, so'rov: {miqdor} dona")
            return

        products[nom]['soni'] -= miqdor
        print(f"OK. {nom} dan {miqdor} dona olib tashlandi. Qolgan: {products[nom]['soni']}")

    except ValueError:
        print("Son kiriting (0 dan katta)")


def list_products():
    if not products:
        print("Ombor bo'sh")
        return

    print("\n{:<15} {:<10} {:<10} {:<15}".format("Nomi", "Narxi", "Soni", "Jami qiymati"))
    print("-" * 50)

    total_value = 0
    for nom, info in products.items():
        jami = info['narxi'] * info['soni']
        total_value += jami
        print("{:<15} {:<10} {:<10} {:<15}".format(
            nom, info['narxi'], info['soni'], jami))

    print("-" * 50)
    print(f"Jami barcha mahsulotlar qiymati: {total_value}")


def main():
    while True:
        display_menu()
        choice = input("Tanlovni kiriting (1-4): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            remove_product()
        elif choice == '3':
            list_products()
        elif choice == '4':
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov! 1-4 oralig'ida son kiriting.")


if __name__ == "__main__":
    main()