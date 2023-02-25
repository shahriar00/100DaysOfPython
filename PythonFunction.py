def myfunction():
    print("This is new function")


myfunction()


def parameter(fname, lname):
    print(fname + " " + lname)


parameter("Alamin", "Asik")


# Arbitrary Arguments, *args
def arbitrary(*kids):
    print(kids[1])


arbitrary("Emil", "Onik")


# Arbitrary Keyword Arguments, **kwargs

def multiarg(**kids):
    print(kids["lname"])


multiarg(fname="Atika", lname="Raisa")


# Passing a List as an Argument

def listpass(foods):
    for x in foods:
        print(x)


fruits = ["apple", "orange", "pineapple"]
print("\nFruits list:")
listpass(fruits)


# Recursion
def try_recursive(k):
    if k > 0:
        result = k + try_recursive(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\nRecursive Result:")
try_recursive(6)
