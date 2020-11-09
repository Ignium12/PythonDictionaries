fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# # del fruit["lemon"]
# # fruit.clear()
# print(fruit["tomato"])
print(fruit)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a {}".format(dict_key))

# ordered_key = list(fruit.keys())
# ordered_key.sort()

# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#   print(f + " - " + fruit[f])


# for val in fruit.values():
#     print(val)
#
# print("-" * 40)
#
# for key in fruit:
#     print(fruit[key])
#
# fruit_keys = fruit.keys()  # view object
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

print(dict(f_tuple))



