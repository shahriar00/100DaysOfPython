tuple1 = ("apple", "mango", "pineapple", "orange", "banana")
tuple2 = ("Red", "Yellow", "normal yellow", "orange color", "normal yellow")
tuple3 = tuple1 + tuple2
# Tuple is order,unchangeable,duplicate values allows
print(len(tuple1))
print(tuple1)
print(tuple1[2:3])
print(tuple1[-3:])

y = list(tuple1)
y.append("jackfruit")
# y.remove("jackfruit")
print(y)

print(tuple3)

# Loop in tuples...

for x in tuple1:
    print(x)