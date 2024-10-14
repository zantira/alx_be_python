#Python script named polymorphism_demo.py. In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.
import math 
#Base class
class Shape:
    def __init__(self):
        ...
    def area(self):
        raise NotImplementedError
    
    
#derived classes

class Rectangle(Shape):
    def area(self, length, width):
        self.length = length
        self.width = width
        return self.length * self.width
    

class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        return math.pi * [radius]**2
    
cirlce = Circle()
print(cirlce.area(7))

# from polymorphism_demo import Shape, Rectangle, Circle
# import math

# def main():
#     shapes = [
#         Rectangle(10, 5),
#         Circle(7)
#     ]

#     for shape in shapes:
#         print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

# if __name__ == "__main__":
#     main()


