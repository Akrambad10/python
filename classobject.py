# Class is a blueprint of an object.
# An object is an instance of a class

class Person:
    # Properties/Attributes/Characteristics
    name = "Bon"
    age = 13
    Location = "Westlands"

    def speak(self):
        print("Person is speaking")


accountant = Person()
print(accountant.age)

accountant.speak()