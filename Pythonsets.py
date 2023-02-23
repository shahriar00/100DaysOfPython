# Set items are unordered, unchangeable, and do not allow duplicate values.

set1 = {"mango", "jackfruit", "apple", "pineapple"}
set2 = {1, 2, 3, 4}
set3 = set1 | set2
set4 = set1 & set2
set5 = set1 - set2

set1.add("orange")
set2.add(6)
set2.add(5)
set2.remove(3)
print(set1)
print(len(set1))
print(set1)
print(set2)
print(set2)
print(set2)
print(set3)
print(set4)
print(set5)

# Set Method:
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# discard()	Remove the specified item
# pop()	Removes an element from the set
# remove()	Removes the specified element
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others
# intersection()	Returns a set, that is the intersection of two other sets
# issubset()	Returns whether another set contains this set or not
