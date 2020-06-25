fruit = {"orange": " a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a small sour, yellow citrus fruit",
         "grape": "a small sweet fruit grown in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)

veg = {"cabbage": "every childe's favorite",
       "sprouts": "mmmm lovely",
       "spinach": "can I have some more fruit place"}

# print(veg)
#
# veg.update(fruit)
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)