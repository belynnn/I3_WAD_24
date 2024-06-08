# page 193

from random import randint


def random_letter():

    possibilities = ["a", "b", "c", "d", "e"]
    index = randint(0, len(possibilities) - 1)

    letter = possibilities[index]

    return letter

# main 

word = ""
for _ in range(5):
    word += random_letter()

print(word)