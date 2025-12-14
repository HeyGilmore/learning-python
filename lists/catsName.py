# Array for cats name
cats = []

print("The List: ", cats[:])

while True:
    print("What is your cats name?")
    catsname = input()
    if catsname == "":
        break
    else:
        cats = cats + [catsname]


if len(cats) != 0:
    print(cats[:])
else:
    print("You dont have any cats")
