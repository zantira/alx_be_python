#Python script named polymorphism_demo.py. In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.
import math 
#Base class
class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
    
    
#derived classes

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

class Circle(Shape):
    def __init__(self, radius):
         super().__init__()
         self.radius = radius
         
    def area(self):
        return math.pi * self.radius**2
    


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


