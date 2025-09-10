from abc import ABC, abstractmethod


class Computer(ABC):
    total_computers = 0

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        Computer.total_computers += 1

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price must be positive")
        self.price = price

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def get_total_computers(cls):
        return cls.total_computers

    def __gt__(self,other):
        return self.get_price() > other.get_price()
    def __lt__(self,other):
        return self.get_price() < other.get_price()
    def __eq__(self,other):
        return self.get_price() == other.get_price()

    def __repr__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.price}$"


class Monoblock(Computer):
    def __init__(self, brand, model, year, price, screen_size):
        super().__init__(brand, model, year, price)
        self.screen_size = screen_size

    def display_info(self):
        return f"Monoblock: {self.brand} {self.model}, {self.year}, {self.price}$, {self.screen_size} ekran"


class Notebook(Computer):
    def __init__(self, brand, model, year, price, battery_life):
        super().__init__(brand, model, year, price)
        self.battery_life = battery_life

    def display_info(self):
        return f"Notebook: {self.brand} {self.model}, {self.year},{self.price}$,{self.battery_life} soat batareya"


class Zavod:
    total_factories = 0

    def __int__(self, name):
        self.name = name
        self.products = []
        Zavod.total_factories += 1

    def add_product(self, product):
        if isinstance(product, Computer):
            self.products.append(product)
        else:
            print("Faqat Computer obyektlarini qo‘shish mumkin!")

    def list_products(self):
        result = []
        for p in self.products:
            result.append(p.display_info())
        return result

zavod = Zavod("Zavod")
pc1 = Monoblock("Dell", "Inspiron", 2020, 800, 27)
pc2 = Notebook("HP", "Pavilion", 2022, 1200, 8)
pc3 = Notebook("Apple", "MacBook Pro", 2023, 2500, 12)

print("Qaysi kompyuter qimmatroq? ", pc3 > pc2)
