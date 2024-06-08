
from random import randint

# Définir fonction
def composate_word(number) :
    LETTERS = ["a", "h", "k", "o", "n", "s", "t"]
    index = randint(0, len(LETTERS) - 1)

    return LETTERS[index]

# Demander une entrée à l'user
number = int(input("Entrez un nombre : "))

# Boucle pour alimenter 'text'
text = ""
for _ in range(number) :
    text += f"{composate_word(number)}"

# Afficher
print(f"{text}")