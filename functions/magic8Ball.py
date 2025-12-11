import random

randomNum = random.randint(1, 10)


def magic8Ball(randomNumber):
    if randomNumber == 1:
        return "Yes!"
    if randomNumber == 2:
        return "Most Likely!"
    if randomNumber == 3:
        return "It is close to happening!"
    if randomNumber == 4:
        return "Might happen!"
    if randomNumber == 5:
        return "I don't think so!"
    if randomNumber == 6:
        return "concentrate and ask again!"
    if randomNumber == 7:
        return "ask again later!"
    if randomNumber == 8:
        return "My reply is no!"
    if randomNumber == 9:
        return "Outlook not so good!"
    if randomNumber == 10:
        return "Nope!"


fortune = magic8Ball(randomNum)

print(fortune)
