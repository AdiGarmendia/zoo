# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("badger", "wolf", "monkey", "gator", "hedgehog",
 "dingo", "rhino", "bear", "tiger", "lion")

# Find one of your animals using the tuple.index(value) syntax on the tuple.
print(zoo.index("rhino")) # Output is 6

# Determine if an animal is in your tuple by using value in tuple syntax
animal_to_find = "gator"
if animal_to_find in zoo:
    # Print that the animal was found
    print(f"{animal_to_find} is here")


    children = ("Sally", "Hansel", "Gretel", "Svetlana")
(first_child, second_child, third_child, fourth_child) = children
print(first_child) # Output is "Sally"
print(second_child) # Output is "Hansel"
print(third_child) # Output is "Gretel"
print(fourth_child) # Output is "Svetlana"

# Create a variable for the animals in your zoo tuple, and print them to the console.
(first_animal, second_animal, third_animal, fourth_animal, fifth_animal,
 sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)

#Convert your tuple into a list.
zoo2 = list(tuple(zoo))

#Use extend() to add three more animals to your zoo.
zoo2.extend(["kangaroo", "dog", "cat"])

#Convert the list back into a tuple.
zoo3 = tuple(list(zoo2))