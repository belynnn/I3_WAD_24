from random import randint


CODE_LENGTH = 4
LETTERS = ["a", "b", "c", "d", "e", "f"]

code = []

while len(code) < CODE_LENGTH:
    index = randint(0, len(LETTERS) - 1)
    letter = LETTERS[index]
    code.append(LETTERS[index])

print(code)