from random import randint

letters = ["a", "b", "c", "d", "e", "f"]

code = []

while len(code) < 4 :
    # ne fonctionnait pas car renvoyait 6 (donc de 0 à 6), au lieu de 5
    # index = randint(0, len(letters))
    index = randint(0, len(letters)-1)

    code.append(letters[index])

print(code)



# ####################################
# # CORRECTION                       #
# ####################################
# from random import randint

# CODE_LENGHT = 4

# LETTERS = ["a", "b", "c", "d", "e", "f"]

# code = []

# while len(code) < CODE_LENGHT :
#     index = randint(0, len(LETTERS) - 1)

#     letter = LETTERS[index]

#     code.append(LETTERS[index])

# print(code)