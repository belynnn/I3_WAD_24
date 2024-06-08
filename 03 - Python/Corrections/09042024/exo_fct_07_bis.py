from random import randint


def random_word(number):

    letters = ["a", "i", "l", "n", "o","r", "s", "t"]
    
    if number > len(letters):
        number = len(letters):

    word = ""

    for _ in range(number):
        index = randint(0, len(letters) - 1)
        word += letters.pop(index)
        
    return word


# --- main program ---

number = input("Combien de lettre: ")
number = int(number)

word = random_word(number)
print(word)