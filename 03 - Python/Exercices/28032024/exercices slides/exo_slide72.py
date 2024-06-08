# Ennoncé
"""
Faire en sorte que le programme génère aléatoirement un nombre à deviner entre 1 et 10.
Demander à l'utilisateur de donner un nombre entre 1 et 10.
Indiquer à l'utilisateur si son nombre est inférieur, supérieur ou égal au nombre à deviner
"""

from random import randint

# Faire en sorte que le programme génère aléatoirement un nombre à deviner entre 1 et 10.
random_number = randint(1,10)

# Demander à l'utilisateur de donner un nombre entre 1 et 10.
user_number = int(input("Entrez un nombre : "))

# Indiquer à l'utilisateur si son nombre est inférieur, supérieur ou égal au nombre à deviner
if user_number < random_number :
    print("Trop petit !")
elif user_number > random_number :
    print("Trop grand...")
else :
    print("OMFG")