from random import randint


def random_word():

    letters = ["a", "i", "l", "n", "o","r", "s", "t"]

    word = ""

    for _ in range(5):
        index = randint(0, len(letters) - 1)
        letter = letters[index]
        word += letter
        letters.remove(letter)

    return word


# --- main program ---

word = random_word()
print(word)