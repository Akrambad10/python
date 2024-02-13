class Shape:
    def draw(self):
        print("Drawing Shape")

class Square:
    def draw(self):
        print("Drawing Square")

class Rectangle:
    def draw(self):
        print("Drawing Rectangle")

sq = Shape|()

s = Square(Shape)
s.
r = Rectangle()