from random import randint

def random_word():
    LETTERS = ["a", "i", "l", "n", "o", "r", "s", "t"]

    word = ""
    for _ in range(5):
        index = randint(0, len(LETTERS) -1)
        word += LETTERS.pop(index)
        
    return word

result = random_word()
print(result)

# CORRECTION

def random_word():
    LETTERS = ["a", "i", "l", "n", "o", "r", "s", "t"]

    word = ""

    for _ in range(5):
        index = randint(0, len(LETTERS) -1)
        letter = LETTERS[index]
        word += letter
        LETTERS.remove(letter)

    return word

#   --- MAIN PROGRAM ---

result = random_word()
print(result)

# def random_word(number) :
#     LETTERS = "ailnorst"
    
#     word = ""
#     for _ in range(number) :
#         letter = LETTERS[randint(0, len(LETTERS) - 1)]
        
#         LETTERS = LETTERS.replace(letter, "")
#         word = word.replace(letter, letter)

#         word += letter

#     return word

# print(random_word(5))



"""
pour chaque lettre dans une itération*5
sélectionner un index aléatoire = lettre
vérifier si la lettre est déjà dans le mot
    si oui > "wrong" et break pour relancer la boucle
    si non > "good" et ajouter au mot attendu
"""
# def random_word(number) :
#     LETTERS = "ailnorst"
#     wrong = ""
#     word = ""
#     while len(word) > number :
#         letter = LETTERS[randint(0, len(LETTERS) - 1)]

#         if letter in word :
#             wrong += letter
#         else :
#             word += letter

#     return word

# print(random_word(5))