# 8 ta boolean,str,float,int,dict,tuple,list,set,person
class Person:
    def __init__(self, name, age, last_name, race, gender):
        self.name = name
        self.age = age
        self.last_name = last_name
        self.race = race
        self.gender = gender

    def malumot_ber(self):
        return f'{self.name} ismli shaxsning yoshi {self.age} irqi {self.race} va uning gender {self.gender} '


shaxs1 = Person(name='Ali', age=20, last_name='Aliyev', race='black', gender='M')
shax2 = Person('Gani', 21, 'asas', 'asas', 'M')

print(shaxs1.name)
# print(shaxs1.name)
# print(shaxs1.age)
print(shaxs1.malumot_ber())
print(shax2.malumot_ber())

salom = 'salom'.title()
print()

class Music:
    pass

class Artist:
    pass
