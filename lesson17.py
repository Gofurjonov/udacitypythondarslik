menu = {
    "osh": 2.5,
    'salat': 1,
    'non': 0.5,
    'choy': 0.5,
    'cola': 1
}

savatcha = {
    # 'osh':2
    # 'salat':2
}


def show_menu():
    count = 1
    for k, v in menu.items():
        print(f'{count} - {k} : {v} $')
        count += 1
    print()


def order(*args, **kwargs):  # 1,2
    global savatcha
    for i in args[0]:
        if i in menu:
            savatcha[i] = 1
        else:
            print(f'{i} menuda mavjud emas afsus!!')


def details_order():
    print('\nsizning zakazlaringiz')
    for k, v in savatcha.items():
        print(f'{k}-{v} portsya')
    print()


def update_order(a):
    global savatcha

    for i in a:
        if i in menu.keys():
            if i in savatcha:
                savatcha[i] += 1
            else:
                savatcha[i] = 1
        else:
            print(f'{i} menuda mavjud emas afsus!!')


def hisob():
    total = 0
    for k, v in savatcha.items():
        total += menu[k] * v
    print(f'umumiy summa {total}')


def main():
    while True:
        choose = int(input(
            '1.menu\n2.buyurtma berish\n3.buyurtma tafsilotlari\n4.Qoshimcha buyurtma\n5.hisobni sorash\n0.Exit\n\nyuqoridagi menyulardan birini tanlang'))
        if choose == 1:
            show_menu()
        elif choose == 2:
            try:
                a = input('menyudagi ovqatlar raqamini kiriting(osh,salat)').split(',')
            except:
                print('xato malumot kiritingiz 1,2,3 raqamlar orasini , bilan ajrating')
                continue
            order(a)
        elif choose == 3:
            details_order()

        elif choose == 4:
            try:
                a = input('menyudagi ovqatlar kiriting(osh,salat)').split(',')
            except:
                print('xato malumot kiritingiz 1,2,3 ovqatlar orasini , bilan ajrating')
                continue

            update_order(a)

        elif choose == 5:
            hisob()
        else:
            break


# if __name__ == '__main__':
#     main()
if __name__ == '__main__':
    main()