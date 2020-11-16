fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sporuts": "mmmm, lovely",
       "spinach": "can i have some more fruit, please?",}


print(veg)

# veg.update(fruit)  # combines the two dictionaries, None is returned
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)