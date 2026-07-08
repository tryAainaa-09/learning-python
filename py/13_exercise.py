#Inheritance
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side
    
circleName = Circle(5)
squareName = Square(4)

print(circleName.area())  # Output: 78.5
print(squareName.area())  # Output: 16

# print(circle.name)  # Output: Circle
# print(square.name)  # Output: Square

# print(f"Area of {circle.name} : {circle.area()}")  # Output: Area of Circle is 78.5
# print(f"Area of {square.name} : {square.area()}")  # Output: Area of Square is 16

#Polymorphism
def print_area(shape):
    print(f"Area of {shape.name} is {shape.area()}")

print_area(circleName)  # Output: Area of Circle is 78.5
print_area(squareName)  # Output: Area of Square is 16

shapes = [Circle(4), Square(5), Circle(6)]
for shape in shapes:
    print_area(shape)