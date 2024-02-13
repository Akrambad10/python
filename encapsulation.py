class car:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model


car1 = car("Toyota", "Camry")
car2 = car("Honda","Civic")

print(car1.get_brand())
print(car2.get_model())

