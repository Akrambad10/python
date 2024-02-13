class Person:
    def __init__(self,firstname,age,gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender

    def details(self):
        print(self.firstname,"is studying")

teacher = Person("Joe",56,"Male")
accountant = Person("Mary",35,"Female")
Doctor = Person("May",35,"Female")

Doctor.details()
print(teacher.firstname,teacher.age,teacher.gender)