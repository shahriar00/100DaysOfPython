class student :
    roll = "",
    name = ""
    def setvalue(self,roll,name):
        self.roll = roll,
        self.name = name
    def display(self):
        return print(f"Roll:{self.roll},name:{self.name}")

# Method........
rahim  = student()
rahim.setvalue(31,"Rahim")
rahim.display()

karim = student()
rahim.setvalue(31,"Karim")
rahim.display()

class Triangle():
    base =""
    height = ""

    def __init__(self,base,height):
        self.base = base
        self.height = height
        area = 0.5*self.base*self.height
        print(area)

Triangle(10,20)