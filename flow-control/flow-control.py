# print()
# print("---------------------")
# print("IF Statements")
# print()
# name = "alice"

# if name == "alice":
#     print("Hello Alice")

# print("---------------------")
# print("IF ElSE Statements")
# print()

# if name == "bob":
#     print("Hey Bob!")
# else:
#     print("Hello Stranger!")

# print()
# print("---------------------")
# print("ELIF Statements")
# print()

# # Checking hours of a store.
# hour = 14

# if hour < 11:
#     print("We are closed")
# elif hour < 20:
#     print("We are open!")
# else:
#     print("We are closed for the night")

# print()
# print("**Bowling Statements**")
# print()

# score = 212

# if score >= 250:
#     print("Great Game!")
# elif score >= 200:
#     print("Solid Game")
# elif score >= 170:
#     print("Decent Game!")
# else:
#     print("Keep Trying!")


# print()
# print("---------------------")
# print("WHILE LOOPS Statements")
# print()

# count = 1

# while count <= 5:
#     print(count)
#     count = count + 1


# print()
# print("** Asking Password **")
# print()

# password = ""

# while password != "midnight":
#     password = input("Emter the correct password: ")

# print("Access Granted!")


# print()
# print("** Loop till quit **")
# print()

# command = "quit"

# while command != "quit":
#     command = input("Type your command: ")

# print("Program ended!")


# print()
# print("** Mini Orderin System **")
# print()


# order = ""

# while order != "done":
#     order = input("What would you like to order? (pizza/wings/drinks/done): ")

#     if order == "pizza":
#         print("Deep dish pizza coming right up!")
#     elif order == "wings":
#         print("Wings on the way!")
#     elif order == "drink":
#         print("What drink would you like?")
#     elif order == "done":
#         print("Order complete!")
#     else:
#         print("Sorry, we don't have that.")


# print()
# print("---------------------")
# print("For Loop and The range() Function")
# print()

# print ("Hey this is a line")
# for i in range(5):
#     print("Bob is counting to: " + str(i))


# print("You can do this in a while loop, jsut rememebr these are tools to use to complete the mission. ")

print()
print("** Starting, Stopping, and Stepping **")
print()

for i in range(12, 16):
    print(i)


print()
print()

for i in range(0, 10, 2):
    print(i)


print()
print()

for i in range(10, -1, -2):
    print(i)

print()
print("** Random Number")
print()


import random

for i in range(10):
    print(random.randint(1, 20))

print()
print("** Ending Program early")
print()

import sys

while True:
    print("Type exit to exit.")
    responce = input()
    if responce == "exit":
        sys.exit()
    print("You typed " + responce + " .")
