#an object is like a blueprint that's used to create
# to describe 2 objects (squares and circles).

class Shape:
    def area(self):
        pass # this is a placeholder that allows us to create empty code.
                #without causing errors.

class Square(Shape):
    def __init__(self, side_length):
        #init is like the constructor. How we define the attributes of the object
        self.side_length = side_length
        def area(self):
            return self.side_length **2
        
import math
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius **2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    
square = Square(5)
print("Area of the Square", square.area())
circle = Circle(3)
print("Area of the Circle", circle.area())
triangle = Triangle(4,5)
triangle2 = Triangle(5,6)
print("the area of the Triangle is", triangle.area())
print("the area of the Triangle is", triangle2.area())

#this is the same as self