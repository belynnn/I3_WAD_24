#page 188

from random import randint


def grettings():
    possibilities = ["ciao", "hello", "ola", "bonjour"]

    index = randint(0, len(possibilities) - 1)

    print(possibilities[index])

# main program

for _ in range(100):
    grettings()

