class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
       return f"{self.name,self.age}"

p = myclass("John",33)

print(p)

# print(p.name)
# print(p.age)
