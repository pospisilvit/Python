class Shape:
    def render(self):
        print("Initializing to render some shape... ")
    
class Square(Shape):
    def render(self):
        super().render()
        print("Rendering Triangle...")

class Triangle(Shape):
    def render(self):
        super().render()
        print("Rendering Triangle")

class Circle(Shape):
    def render(self):
        super().render()
        print("Rendering Circle...")

class Oval(Shape):
    def render(self):
        super().render()
        print("Rendering Oval...")

s1 = Square()
s1.render()

t1 = Triangle()
t1.render()

c1 = Circle()
c1.render()

o1 = Oval()
o1.render()

class Factory:

    __article = ["Square", "Triangle", "Circle", "Oval"]

    @staticmethod
    def create(representative):

        if representative in Factory.__article:
            return globals()[representative]()
        else:
            return Square()
        
my_square = Factory.create("Square")
my_square.render()

my_triangle = Factory.create("Triangle")
my_triangle.render()

my_circle = Factory.create("Circle")
my_circle.render()

my_oval = Factory.create("Auto")
my_oval.render()