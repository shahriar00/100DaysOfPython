class shape:
    def __init__(self):
        print("I am inside Shape Class")

class Rectangle:
    def area(self):
        print("I am inside Rectangle")

class Triangle(shape,Rectangle):
    pass



t = Triangle()
t.area()