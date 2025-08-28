# class LibraryItem:
#     def __init__(self, title, upc, subject):
#         self.title = title
#         self.upc = upc
#         self.subject = subject
#
#     def locate(self):
#         return f"Locating item: {self.title}"
#
#
# class Book(LibraryItem):
#     def __init__(self, title, upc, subject, isbn, authors, dds_number):
#         super().__init__(title, upc, subject)
#         self.isbn = isbn
#         self.authors = authors  # list of Author
#         self.dds_number = dds_number
#
#
# class Magazine(LibraryItem):
#     def __init__(self, title, upc, subject, volume, issue):
#         super().__init__(title, upc, subject)
#         self.volume = volume
#         self.issue = issue
#
#
# class DVD(LibraryItem):
#     def __init__(self, title, upc, subject, actors, director, genre):
#         super().__init__(title, upc, subject)
#         self.actors = actors
#         self.director = director
#         self.genre = genre
#
#
# class CD(LibraryItem):
#     def __init__(self, title, upc, subject, artist):
#         super().__init__(title, upc, subject)
#         self.artist = artist
#
#
# class Author:
#     def __init__(self, name):
#         self.name = name
#
#
# class Catalog:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def search(self, title):
#         results = [item for item in self.items if title.lower() in item.title.lower()]
#         return results
#
#
# # =====================
# # Misol uchun ishlatish
# # =====================
#
# author1 = Author("Abdulla Avloniy")
# book1 = Book("Komil Inson", "12345", "Philosophy", "ISBN123", [author1], "DDS100")
#
# dvd1 = DVD("Inception", "67890", "Science Fiction", ["Leonardo DiCaprio"], "Christopher Nolan", "Sci-Fi")
#
# catalog = Catalog()
# catalog.add_item(book1)
# catalog.add_item(dvd1)
#
# # Qidiruv
# results = catalog.search("Komil")
# for item in results:
#     print(f"Topildi: {item.title}, Subject: {item.subject}")

class Avto:
     def __init__(self, model, rang, korobka, narh, kilometer=0):
        """Avtomobil xususiyatlari"""
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometer = kilometer

    def get_info(self):
        info = f"Model: {self.model}, Rangi: {self.rang}, "
        info += f"Korobka: {self.korobka}, Narhi: ${self.narh}, "
        info += f"Kilometraj: {self.kilometer} km"
        return info

    def update_km(self, yangi_km):
        """Kilometrajni yangilash"""
        if yangi_km >= self.kilometer:
            self.kilometer = yangi_km
        else:
            print("Kilometrajni kamaytirib bo'lmaydi!")


class Avtosalon:
    """Avtosalon klassi"""

    def __init__(self, nomi, manzili):
        """Avtosalon xususiyatlari"""
        self.nomi = nomi
        self.manzili = manzili
        self.avtomobillar = []

    def add_avto(self, avto):
        """Yangi avtomobil qo'shish"""
        self.avtomobillar.append(avto)
        print(f"{avto.model} avtomobili qo'shildi")

    def get_avto_info(self):
        """Barcha avtomobillar haqida ma'lumot"""
        if not self.avtomobillar:
            return "Avtosalon bo'sh"

        info = f"{self.nomi} avtosaloni ({self.manzili})\n"
        info += "Avtomobillar ro'yxati:\n"
        for idx, avto in enumerate(self.avtomobillar, 1):
            info += f"{idx}. {avto.get_info()}\n"
        return info


# Test qilish
if __name__ == "__main__":
    # Avto obyektlarini yaratamiz
    avto1 = Avto("Toyota Camry", "Oq", "Avtomat", 25000, 15000)
    avto2 = Avto("Honda Civic", "Qora", "Mexanika", 22000)
    avto3 = Avto("Tesla Model 3", "Kumush", "Avtomat", 45000, 5000)

    # Avto metodlarini test qilamiz
    print("=== Avto metodlari testi ===")
    print(avto1.get_info())
    print(avto2.get_info())

    # Kilometrajni yangilaymiz
    avto1.update_km(18000)
    print("Yangilangan kilometraj:", avto1.kilometer)

    # Noto'g'ri kilometraj testi
    avto1.update_km(10000)  # Bu xato beradi

    # Avtosalon yaratamiz
    salon = Avtosalon("Super Avto", "Toshkent shahri")

    # Avtomobillarni salon ga qo'shamiz
    salon.add_avto(avto1)
    salon.add_avto(avto2)
    salon.add_avto(avto3)

    # Salon ma'lumotlarini ko'ramiz
    print("\n=== Avtosalon ma'lumotlari ===")
    print(salon.get_avto_info())

    # dir() va __dict__ metodlarini tekshiramiz
    print("\n=== dir() va __dict__ metodlari ===")

    # Avto klassining metodlari
    print("Avto klass metodlari:")
    print(dir(Avto))
    print("\nAvto obyektining xususiyatlari:")
    print(avto1.__dict__)

    # Pythondagi boshqa klasslarning metodlari
    print("\nstr klassining metodlari:")
    print([method for method in dir(str) if not method.startswith('_')][:10])

    print("\nint klassining metodlari:")
    print([method for method in dir(int) if not method.startswith('_')][:10])

    # Avtosalon obyektining xususiyatlari
    print("\nAvtosalon obyektining xususiyatlari:")
    print(salon.__dict__)