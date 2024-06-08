# Importation de la fonction randint
from random import randint

# # Définition de la fonction servant à un composer un mot par rapport à une liste de caractères
# def composate_word(number) :
#     LETTERS = ["a", "h", "k", "o", "n", "s", "t"]
#     index = randint(0, len(LETTERS) - 1)

#     return LETTERS[index]

# # Demander une entrée à l'user
# number = int(input("Entrez un nombre : "))

# # Mise en place d'une boucle for pour alimenter 'text' en fonction du nombre envoyé par l'utilisateurice
# text = ""
# for _ in range(number) :
#     text += f"{composate_word(number)}"

# # Affichage
# print(f"{text}")



####################################
# CORRECTION                       #
####################################
# ATTENTION énnoncé : il était demandé de fabriqué le mot DANS la fonction "fabriqué par la fonction"
def random_word(number_letters) :
    LETTERS = ["a", "h", "k", "o", "n", "s", "t"]
    word = ""
    
    for _ in range(number_letters) :
        index = randint(0, len(LETTERS) - 1)
        letter = LETTERS[index]
        word += letter

    return word

user_number = int(input("Entrez un nombre : "))
result = random_word(user_number)

print(result)