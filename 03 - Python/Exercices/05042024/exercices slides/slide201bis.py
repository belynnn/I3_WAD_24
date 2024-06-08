from random import randint

def random_letter() :
    LETTERS = ["a", "h", "k", "o", "n", "s", "t"]
    index = randint(0, len(LETTERS)-1)
    letter = LETTERS[index]

    return letter

def random_word(number_letters) :
    word = ""

    for _ in range(number_letters) :
        word += random_letter()

    return word

user_number = int(input("Entrez un nombre : "))
result = random_word(user_number)

print(result)