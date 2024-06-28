from random import randint

code = ""

def rand_letter():
    letters = ["a", "b", "c", "d", "e"]
    index_in_letters = randint(0, len(letters)-1)
    letter = letters[index_in_letters]
    return letter

for i in range(5):
    code = code + rand_letter()

print("code = " + code)
a = randint(0, 100)
