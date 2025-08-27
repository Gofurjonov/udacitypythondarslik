#
# p1 = Person('Ali',14,'vali','black','F')
#
# print(p1.gender) #M

class Subject:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours


subject1 = Subject('Math', 150)
subject2 = Subject('English', 100)
subject3 = Subject('C++', 150)


class Student:
    def __init__(self, fullname, age, gender='M'):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.step = 1
        self.subject = []


    def set_step(self, course):
        if course < 0:
            return 'XATOLIK 0 dan kichik course kirta olmasiz'
        else:
            self.step = course  # objectni stepi update bolyapti
            return self.step

    def subject_info(self):
        print(self.get_info())
        for i in self.subject:
            print(f'{i.name}- bosqich {i.hours}')

    def get_info(self):
        return f'{self.fullname} - bosqich {self.step}'

s1 = Student('Ali Valiyev', 21)

# s1.age = 23 bu obyetni xususaytini qiymatini ozgartirish

# print(s1.set_step(-2))
print(s1.subject)
s1.subject = [subject1, subject2, subject3]

print(s1.subject)
