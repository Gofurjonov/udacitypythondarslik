# import csv
# age = 0
# with open('person.csv', 'w', newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(['age', 'name', 'surname'])
#     writer.writerow([21, 'Ali', 'Valiyev'])
#     writer.writerow([25, 'Alish', 'Valiyev'])
#     writer.writerow([32, 'Aliya', 'Valiyev'])
#
#
# with open('person.csv', 'r') as f:
#     reader = csv.reader(f)
#     for index, row in enumerate(reader):
#         if index == 0:
#             continue
#         age += int(row[0])
# print(age/index)
#
# with open('person.csv', 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(['37', 'Asal', 'Valiyev'])

import csv

filename = "talabalar.csv"


class Talaba:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return f"{self.surname}{self.name}, {self.age} yosh"


class Universitet:
    def __init__(self, univer_nomi):
        self.univer_nomi = univer_nomi
        self.talabalar = []

    def add_talaba(self, talaba):
        if isinstance(talaba, Talaba):
            self.talabalar.append(talaba)
        else:
            raise TypeError("Xatolik")

    def get_talabalar(self):
        return self.talabalar

    def save_talaba(self, filename="talabalar.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['Familiya', 'Ismi', 'Yosh'])
            for i in self.talabalar:
                writer.writerow([i.surname, i.name, i.age])


def menu():
    univer = input("Universitet nomi: ")
    universitet = Universitet(univer)
    while True:
        print("\n1.Talaba qo'shish")
        print("2.Talabalar ro'yhati")
        print("3.Csv ga yozish")
        print("4.Exit")

        tanla = input("Tanlaganizni kiriting: ")

        if tanla == '1':
            name = input("Talabaning ismi: ")
            surname = input("Talabaning familiyasi: ")
            age = input("Talabaning yoshi: ")
            universitet.add_talaba(Talaba(name, surname, age))
            print("Talaba qo'shildi")
        elif tanla == '2':
            talabalar = universitet.get_talabalar()
            if talabalar:
                print("\nTalabalar ro'yhati: ")
                for t in talabalar:
                    print(t)
            else:
                print("Hali talabalar yo'q! ")

        elif tanla == '3':
            universitet.save_talaba()
            print("Talabalar 'talabalar csvga qoshildi'")
        elif tanla == '4':
            break
        else:
            print("Menyuda yoq")

if __name__ == '__main__':
    menu()