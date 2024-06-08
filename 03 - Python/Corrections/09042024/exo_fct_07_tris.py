from random import randint


def random_word(number, letters):

    if number > len(letters):
        number = len(letters)
    
    word = ""

    for _ in range(number):
        index = randint(0, len(letters) - 1)
        word += letters.pop(index)
        
    return word


# --- main program ---

letters = ["a", "e", "v", "t", "d"]
number = input("Combien de lettre: ")
number = int(number)

word = random_word(number, letters)
print(word)