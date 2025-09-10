class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yoshda"

    def __str__(self):
        return self.get_info()


class Fan:
    def __init__(self, nomi, kredit):
        self.nomi = nomi
        self.kredit = kredit

    def __str__(self):
        return f"{self.nomi} ({self.kredit} kredit)"


class Talaba(Shaxs):
    def __init__(self, ism, familiya, yosh, student_id):
        super().__init__(ism, familiya, yosh)
        self.student_id = student_id
        self.fanlar = []  # Bo'sh ro'yxat

    def fanga_yozil(self, fan):
        if isinstance(fan, Fan):
            self.fanlar.append(fan)
            print(f"{fan.nomi} faniga yozildingiz")
        else:
            print("Fan obyekti kiritishingiz kerak")

    def remove_fan(self, fan_nomi):
        for fan in self.fanlar:
            if fan.nomi == fan_nomi:
                self.fanlar.remove(fan)
                print(f"{fan_nomi} fanidan o'chirildingiz")
                return

        print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        fanlar_list = ", ".join([fan.nomi for fan in self.fanlar]) if self.fanlar else "fanlar yo'q"
        return f"{super().get_info()}, ID: {self.student_id}, Fanlar: {fanlar_list}"


class Professor(Shaxs):
    def __init__(self, ism, familiya, yosh, mutaxassislik, maosh):
        super().__init__(ism, familiya, yosh)
        self.mutaxassislik = mutaxassislik
        self.maosh = maosh

    def get_info(self):
        return f"{super().get_info()}, {self.mutaxassislik} mutaxassisi, Maosh: {self.maosh}"

    def dars_berish(self):
        print(f"{self.ism} {self.familiya} dars bermoqda...")


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, username, email):
        super().__init__(ism, familiya, yosh)
        self.username = username
        self.email = email
        self.faol = True

    def get_info(self):
        holat = "Faol" if self.faol else "Nofaol"
        return f"{super().get_info()}, Username: {self.username}, Email: {self.email}, Holat: {holat}"

    def post_yaratish(self, sarlavha):
        print(f"{self.username} yangi post yaratdi: {sarlavha}")


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, yosh, username, email, admin_darajasi):
        super().__init__(ism, familiya, yosh, username, email)
        self.admin_darajasi = admin_darajasi

    def get_info(self):
        return f"{super().get_info()}, Admin darajasi: {self.admin_darajasi}"

    def ban_user(self, foydalanuvchi):
        if isinstance(foydalanuvchi, Foydalanuvchi):
            foydalanuvchi.faol = False
            print(f"Foydalanuvchi {foydalanuvchi.username} bloklandi")
        else:
            print("Noto'g'ri foydalanuvchi obyekti")


class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, dokon_nomi, mahsulotlar):
        super().__init__(ism, familiya, yosh)
        self.dokon_nomi = dokon_nomi
        self.mahsulotlar = mahsulotlar

    def get_info(self):
        return f"{super().get_info()}, Do'kon: {self.dokon_nomi}, Mahsulotlar: {len(self.mahsulotlar)} ta"

    def mahsulot_qoshish(self, yangi_mahsulot):
        self.mahsulotlar.append(yangi_mahsulot)
        print(f"Yangi mahsulot qo'shildi: {yangi_mahsulot}")


class Mijoz(Shaxs):
    def __init__(self, ism, familiya, yosh, telefon, manzil):
        super().__init__(ism, familiya, yosh)
        self.telefon = telefon
        self.manzil = manzil
        self.buyurtmalar = []

    def get_info(self):
        return f"{super().get_info()}, Telefon: {self.telefon}, Manzil: {self.manzil}"

    def buyurtma_berish(self, mahsulot):
        self.buyurtmalar.append(mahsulot)
        print(f"{mahsulot} buyurtma qilindi")


# Test qilish
if __name__ == "__main__":
    # Fan obyektlari yaratish
    matematika = Fan("Matematika", 6)
    fizika = Fan("Fizika", 5)
    informatika = Fan("Informatika", 4)

    # Talaba obyekti
    talaba1 = Talaba("Ali", "Valiyev", 20, "ST123")
    print(talaba1.get_info())

    # Talabani fanga yozish
    talaba1.fanga_yozil(matematika)
    talaba1.fanga_yozil(fizika)
    print(talaba1.get_info())

    # Fandan o'chirish
    talaba1.remove_fan("Fizika")
    print(talaba1.get_info())

    # Yo'q fanni o'chirish
    talaba1.remove_fan("Tarix")

    print("\n" + "=" * 50 + "\n")

    # Professor obyekti
    professor1 = Professor("Dilshod", "Rahimov", 45, "Matematika", 5000000)
    print(professor1.get_info())
    professor1.dars_berish()

    print("\n" + "=" * 50 + "\n")

    # Foydalanuvchi va Admin obyektlari
    user1 = Foydalanuvchi("Hasan", "Husanov", 25, "hasan123", "hasan@mail.com")
    admin1 = Admin("Admin", "Adminov", 30, "superadmin", "admin@mail.com", "Bosh admin")

    print(user1.get_info())
    print(admin1.get_info())

    admin1.ban_user(user1)
    print(user1.get_info())

    print("\n" + "=" * 50 + "\n")

    # Sotuvchi va Mijoz obyektlari
    sotuvchi1 = Sotuvchi("Bobur", "Jo'rayev", 35, "Texnika do'koni", ["Telefon", "Noutbuk", "Planshet"])
    mijoz1 = Mijoz("Olim", "Karimov", 28, "+998901234567", "Toshkent shahar")

    print(sotuvchi1.get_info())
    print(mijoz1.get_info())

    mijoz1.buyurtma_berish("Telefon")
    sotuvchi1.mahsulot_qoshish("Televizor")
    print(sotuvchi1.get_info())