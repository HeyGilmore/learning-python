# Basic Functions


def hello():
    print()
    print("Howdy")
    print()


hello()

# Adding a argument


def intro(name):
    print(f"Hello {name}")


intro("bob")


# Dealing with NONE

# None deals with the absence of a value. the only value of the NoneType data type
# Other languages call this NULL, NIL, UNDEFINED

spam = print("Boss")

print(None == spam)

# End keyword

print("\nHello", end="")
print("WORLD!")

# sep keyword

print("cats", "dogs", "mice")
print("cats", "dogs", "mice", sep=",")


# Stacking functions
print()
print("___Stacking Functions___")
print()


def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

print()
print()
print("___LOCAL AND GLOABL SCOPE___")

# LOcAL AND GLOBAL SCOPE

def spam():
    eggs = 31337
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(eggs)

spam()


def breakfast():
    print("eggs01 "+str(eggs))
eggs = 42
breakfast()
print("eggs02 "+ str(eggs))


print()
print()
print("___Exception Handling___")

def spam(divideBy):
    return 42 / divideBy

