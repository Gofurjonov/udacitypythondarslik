# class Avto:
#     def __init__(self,model,rang,korobka,narh, kilometer=0):
#         self.modal = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narh = narh
#         self.kilometer = kilometer
#
#     def get_info(self):
#         return f'Model: {self.model}, Rangi: {self.rang}, Korobka: {self.korobka}, Narhi: ${self.narh}, Kilometraj: {self.kilometer} km'
#
#     def update_km(self,km):
#         if km < 0:
#             return "Xatolik"
#         else:
#             return self.km+=km
#
#
# # print(avto1.get_info())
#
# class Avtosalon:
#         def __init__(self, nomi, manzili):
#             self.nomi = nomi
#             self.manzili = manzili
#             self.avtomobillar = []
#
#         def add_avto(self, avto):
#             self.avtomobillar.append(avto)
#             print(f"{avto.model} avtomobili qo'shildi")
#
#
# avto1 = Avto("Toyota Camry", "Oq", "Avtomat", 25000, 15000)
# avto2 = Avto("Honda Civic", "Qora", "Mexanika", 22000)
# avto3 = Avto("Tesla Model 3", "Kumush", "Avtomat", 45000, 5000)
#
# print(avto3.add_a)
class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f'{self.ism} {self.familiya} {self.yosh}'


class Talaba:
    def __init__(self, ism, familiya, yoshi):
        self.ism = ism
        self.familiya = familiya
        self.yoshi = yoshi
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
        print(f'{self.ism} {fan.nomi} fanga yozildi')

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            print(f'{fan.nomi} fani ochirildi')
        else:
            print("siz bu fanga yozilmagansiz")

    def get_info(self):
        return f'Ismi: {self.ism} familiyasi {self.familiya} yoshi {self.yoshi}'


class Fan:
    def __init__(self, nomi, kredit):
        self.nomi = nomi
        self.kredit = kredit

    def get_info(self):
        return f'Fan nomi: {self.nomi} krediti: {self.kredit}'


class Professor(Shaxs):
    def __init__(self, ismi, familiya, yosh, mutaxassislik, maosh):
        super().__init__(ismi, familiya, yosh)
        self.mutaxassislik = mutaxassislik
        self.maosh = maosh

    def get_info(self):
        return f"{super().get_info()}, {self.mutaxassislik} mutaxassisi, Maosh: {self.maosh}"

    def dars_berish(self):
        print(f"{self.ism} {self.familiya} dars bermoqda...")


matematika = Fan("Matematika", 6)
fizika = Fan("Fizika", 5)
talaba1 = Talaba("Ali", "Valiyev", 20)

print(talaba1.get_info())
print(fizika.get_info())
talaba1.fanga_yozil(matematika)
print(talaba1.get_info())

talaba1.remove_fan("Fizika")
print(talaba1.get_info())

professor1 = Professor("Dilshod", "Rahimov", 45, "Matematika", 5000000)
print(professor1.get_info())
professor1.dars_berish()

print(dir(int))