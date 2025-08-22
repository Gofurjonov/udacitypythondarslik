class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def getinfo(self):
        return f'Foydalanuvchi ismi: {self.username}, ismi: {self.name}, email: {self.email}'

foydalanuvchi1 = User(name="davikuz", username="Davronbek Gofurjonov", email="gafurjonovdavronbek@gmail.com")
foydalanuvchi2 = User("malika98", "Malika Karimova", "malika98@yahoo.com")

print(foydalanuvchi1.getinfo())
print(foydalanuvchi2.getinfo())
