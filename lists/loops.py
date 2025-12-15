fun_list = [
    "Pizza",
    "Bowling",
    "Acting",
    "Coding",
    "Gym",
    "Video Games",
    "Comedy",
    "Traveling",
    "Photography",
    "Coffee",
    "Learning",
    "Midnight Slice",
    "Short Films",
    "Self Growth",
    "Discipline",
]

print()
print()

# Basic looping

for i in range(4):
    print(fun_list[i])

print()
print()

# Show all in the loop
print("My Fun List:")
for i in range(len(fun_list)):
    print("#" + str(i + 1), fun_list[i])

print()
print()

# Check to see if something is in the array
print("Is Coffee in my fun list:")
isIt = "☕ Coffee" in fun_list
isItNew = "Coffee" in fun_list
print("☕ Coffee is in the list: ", isIt)
print("Coffee is in the list: ", isItNew)

print()
print()

# To make sure something is NOT in the lists
print("Basketball is not in the list right?")
isNotInIt = "Basketball" not in fun_list
print(isNotInIt)


print()
print()

# Let the user see if we have any matching items in the fun list.
print("Please put in an item and lets see if we have things in common: ")
userInput = input().strip().capitalize()

areWeCool = userInput in fun_list
print("Do we have things in common: ", areWeCool)

print()
print()
