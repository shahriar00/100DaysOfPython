from abc import ABC,abstractmethod
class shape(ABC):
    dim1 = ""
    dim2 = ""

    def __init__(self,dim1,dim2):
        self.dim1 = dim1,
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def area(self):
        areadata = "This is a area calculator"
        print(areadata)

        
r = Rectangle(2,1)
r.area()



