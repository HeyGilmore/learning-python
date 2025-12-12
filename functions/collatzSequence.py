def collatz(number):
    intNum = int(number)
    print("current number:", number)
    print("int number:", intNum)

    while intNum != 1:
        if intNum % 2 == 0:
            intNum = intNum // 2
        else:
            intNum = 3 * intNum + 1
        print("Number:", intNum)


print("Give me a number:")
userNumber = input()

try:
    collatz(userNumber)
except ValueError:
    print("Error: You must enter a number.")
except KeyboardInterrupt:
    print("Program interrupted by user.")
