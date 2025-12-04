# Importing Random to generate the lucky number
import random

print()
print("-----------------------------------------")
print("Welcome to guess the lucky number!")
print("-----------------------------------------")
print()
print(
    "The game is easy! You just have to guess a random number that I between the numbers of 1 to 10."
)
# Instruction on how to play.
print()
print("---------------Instructions------------")
print(
    "Once you have guessed the correct lucky number, You will be shown the number of guesses it took you."
)
print("If you would like to quit the game say 'pineapple'.")
print()
print("---------------------------")
# Is the User ready to play?
print("Are you ready to play? (yes/no)")
areYouPlaying = input()
print("---------------------------")
print()


# variables - lucky number, users guess, and count of guesses
luckyNumber = str(random.randint(1, 9))
guesses = 0
usersNumber = 0

# Condition on whether the user would like to play or not
if areYouPlaying.lower() == "yes":
    print("Welcome and lets play!")
    print()
    print()

    # Prenting Loading PAge
    for i in range(1, 4):
        print("------LOADING...------")
        print()

    print()
    print()
    print("------------------------------------------------")
    print()

    # Asking Wuestion
    print("I am thinking of a number between 1 and 10.")
    print("Ready")
    print("Set")
    print("Go")

    print()
    print("------------------------------------------------")
    print()

    # Condition to conitnue till the user either says pineapple or says the correct number
    while str(usersNumber) != str(luckyNumber):
        print()
        print()
        print("What is your number?")
        usersNumber = input()
        # Counts your guesses
        guesses += 1
        # This checks to see if user didn't put a number
        try:
            # If user wants to quit the game
            if usersNumber == "pineapple":
                break

            # Changes user input to int
            int(usersNumber)

            # IF the User guess correctly then this message will show.
            if int(usersNumber) == int(luckyNumber):
                print()
                print("*************************************************")
                print()
                print("CONGRATS!!!! You did it. ")
                print("You guess correctly and only in __" + str(guesses) + "_ tries!")
                print()
                print("*************************************************")
                print()
                print()

        except ValueError:
            print()
            print("****That is NOT a valid number. That still counts as a guess.***")
            continue

else:
    print()
    print("Okay well we tried, BYE!!!!!!!")
    print()


print("----------GAMEOVER---------------")
print()
