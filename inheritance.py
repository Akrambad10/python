# Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Child Class
class Cat(Dog):
    def meow(self):
        print("Cat is meowing")

a = Animal()
d = Dog()

c = Cat()
c.speak()