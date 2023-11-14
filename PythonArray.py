# Python does not have built-in support for Arrays, but Python Lists can be used instead.
fruits = ["Apple","Orange","Mango","Pineapple"]
num = [2,3,5,6,7,8]

add_items = fruits.append("Graps")
one_items_delete = fruits.pop()
copy_item = fruits.copy()
length = len(fruits)
remove_items = num.remove(5)

print(add_items)
print(one_items_delete)
print(copy_item)
print(length)
print(remove_items)


print("Fruits List:\n")
for x in fruits:
    print(x)
