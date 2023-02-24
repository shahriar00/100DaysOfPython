
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and indexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

dictionary = {
    "name":"orange",
    "color":"orangecolor",
    "price":"213"
}
# print(dictionary)
# print(dictionary.values())
# print(dictionary.keys())
# dic = dictionary.update({"price":"222"})
# print(dictionary)

# print(type(dictionary))
# copy_dic = dictionary.copy()
# print(copy_dic)

# for y in dictionary.keys():
#     print(y)
#
# for x in dictionary.values():
#     print(x)

# delete_dic = dictionary.pop("color")
# print(delete_dic)
# print(dictionary)

# Nested Dictionary......

nest = {
    "Bird1":{
        "name":"Bird",
        "color":"Blue",
        "price":"226"
    },
    "Bird2":{
        "name": "RedBird",
        "color": "Red",
        "price": "289"
    }

}
print(nest["Bird1"]["name"])

