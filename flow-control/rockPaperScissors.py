import random

randomNumber = 0
cpu_weapon = ""
user_weapon = ""
winTotal = 0
loseTotal = 0
tieTotal = 0

# Variables


print()
print()
print("___________Welcome To Rock Paper & Scissors___________")
print()
print()

print("*** How to Play ***")
print()
print(
    "First you choose what weapon you would like to use by seceleting (r) for rock, (s) for scissors, and (p) for paper. Once decided then hit enter. The counter would start, then you will see if you won the battle or not. "
)
print("We will keep record of how many times you lose, win, and tie. ")
print("So best of luck!")
print()
print()

print("are you ready? y/n")
startGame = input()
print(startGame)


if startGame == "y":

    while startGame.lower() == "y":
        print()
        print("***** NEW GAME *****")
        userInput = ""

        while userInput != "p" and userInput != "r" and userInput != "s":
            print()
            print("Choose your weapon:")
            print("s - Scissors")
            print("p - Paper")
            print("r - Rock")
            userInput = input()

        match userInput.lower():
            case "r":
                user_weapon = "rock"
            case "s":
                user_weapon = "scissors"
            case "p":
                user_weapon = "paper"

        randomNumber = str(random.randint(1, 3))
        match int(randomNumber):
            case 1:
                cpu_weapon = "rock"
            case 2:
                cpu_weapon = "scissors"
            case 3:
                cpu_weapon = "paper"

        print()
        print("_______RESULTS:______")
        print()
        print("3")
        print("2")
        print("1")
        print()
        print("SHOOT!")
        print()
        if (
            user_weapon == "rock"
            and cpu_weapon == "rock"
            or user_weapon == "scissors"
            and cpu_weapon == "scissors"
            or user_weapon == "paper"
            and cpu_weapon == "paper"
        ):
            print(
                "tied", "\nyour Weapon:", user_weapon, " Computer Weapon: ", cpu_weapon
            )
            tieTotal = tieTotal + 1
        elif (
            user_weapon == "scissors"
            and cpu_weapon == "rock"
            or user_weapon == "rock"
            and cpu_weapon == "paper"
            or user_weapon == "paper"
            and cpu_weapon == "scissors"
        ):
            print(
                "computer wins!",
                "\nyour Weapon:",
                user_weapon,
                " Computer Weapon: ",
                cpu_weapon,
            )
            loseTotal = loseTotal + 1
        elif (
            user_weapon == "paper"
            and cpu_weapon == "rock"
            or user_weapon == "scissors"
            and cpu_weapon == "paper"
            or user_weapon == "rock"
            and cpu_weapon == "scissors"
        ):
            print(
                "You wins!",
                "\nyour Weapon:",
                user_weapon,
                " Computer Weapon: ",
                cpu_weapon,
            )
            winTotal = winTotal + 1
        print()

        print("Wins: ", winTotal, " Loses: ", loseTotal, "Ties: ", tieTotal)
        print()
        print()

        print("Would you like to play again? y/n")
        startGame = input()
        while startGame != "y" and startGame != "n":
            print()
            print("Invalid Answer")
            print()
            print("Would you like to play again? y/n")
            startGame = input()


print("Thank you trying. We will see you soon")
