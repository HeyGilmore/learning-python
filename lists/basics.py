movies = [
    "the matrix",
    "inception",
    "gladiator",
    "the dark knight",
    "fight club",
    "interstellar",
    "john wick",
    "the godfather",
    "pulp fiction",
    "scarface",
]

print()
print("Movies List:")
print()
print(movies[0])
print(movies[1])
print(movies[2])
print(movies[3])
print(movies[4])
print(movies[5])
print(movies[6])
print(movies[7])
print(movies[8])
print(movies[9])


print()
print("______Using NUmbers______")
print()
print(movies[0])


print(movies[int(3.0)])
print(movies[int(3.5)])


print()
print("______Using Nesting Lists______")
print()


players = [["Warrior", 100, "Sword"], ["Mage", 70, "Staff"], ["Rogue", 85, "Daggers"]]

print()
print("players 1: ", players[0])
print("players 1 name: ", players[0][0])
print("players 1 Weapon: ", players[0][2])
print("players 1 Health: ", players[0][1])
print()
print("players 2: ", players[1])
print("players 1 name: ", players[1][0])
print("players 1 Weapon: ", players[1][2])
print("players 1 Health: ", players[1][1])
print()


#  Dealing With negative numbers

print()
print("______Using Negative NUmbers______")
print()
print("movies -3: ", movies[-3])
print("movies -5: ", movies[-5])
print("movies -1: ", movies[-1])

print()
print()
print()

#  GETTING A LIST INSIDE A LIST WITH SLICES

print()
print("______TIME TO SLICE UP THE LIST______")
print()
print("Slicing 1-4: ", movies[1 - 4])
print("Slicing 3-5: ", movies[3:5])
print("Slicing -1 to -3: ", movies[-1:-3])
print("Slicing 0 to -5: ", movies[0:-5])
print("Slicing :-5: ", movies[:-5])
print("Slicing 1: : ", movies[1:])
print("Slicing : -5: ", movies[:])
print("How many in the list: ", len(movies))

print("Before Changing: #3", movies[2])
movies[2] = "Fred Clause"
print("After Changing: #3", movies[2])

print()
print()
print()

#  Deleting Items from list

print()
print("______Deleting items from THE LIST______")
print()

sports = ["basketball", "football", "baseball", "soccer", "bowling", "boxing"]
pizza_toppings = ["pepperoni", "sausage", "bacon", "pineapple", "spinach"]


combo = sports + pizza_toppings

print("2 different list combined :", combo)
print()
print("before deletion:", combo)
del combo[0:6]
print("after deletion:", combo)
print()
print()

