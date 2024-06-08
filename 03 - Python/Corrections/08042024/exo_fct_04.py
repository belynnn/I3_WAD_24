from random import randint


def rnd_numbers(n):
    numbers = []

    for _ in range(n):
        numbers.append(randint(1, 6))

    return numbers


# -- main program --

table = rnd_numbers(18)
print(table)

