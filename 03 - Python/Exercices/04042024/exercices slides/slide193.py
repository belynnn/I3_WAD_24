from random import randint

# def random_code() :
#     LETTERS = ["a", "b", "c", "d", "e"]
#     index = randint(0, len(LETTERS)-1)

#     return LETTERS[index]

# text = ""
# for _ in range(5) :
#     text += f"{random_code()}"

# print(f"{text}")



####################################
# CORRECTION                       #
####################################

def random_letter() :
    POSSIBILITIES = ["a", "b", "c", "d", "e"]
    index = randint(0, len(POSSIBILITIES)-1)

    letter = POSSIBILITIES[index]

    return letter

word = ""
for _ in range(5) :
    word += f"{random_letter()}"

print(f"{word}")