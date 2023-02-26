# A lambda function is a small anonymous function.
x = lambda a: a * a
print(x(2))

y = lambda a, b: a - b
print(y(5, 2))

z = lambda a, b, c: a + b + c
print(z(1, 3, 5))


def myfunction(n):
    return lambda a: a * n


mydoubler = myfunction(2)

print(mydoubler(23))
