"""
#! énoncé
Dans un autre script :

Écrivez un programme qui va générer trois nombres aléatoirement (entre 1 et 6).
Ensuite le programme va afficher les trois nombres
Si les trois nombres ne sont pas identiques, il recommence.

#! décripteur Belynn1312
#? Importer randint
#? Instancier 3 variables qui vont contenir des valeurs numériques
#? Dans chaque variable, valeurs numérique aléatoire entre 1 et 6
#? Initialiser un bloc d'instruction BOUCLE TANT QUE
#?      Afficher les 3 nombres
#?      TANT QUE les nombres ne sont pas identique
#?          Continuer
"""

from random import randint

def random_number() :
    number = randint(1,6)

    return number

number1 = random_number()
number2 = random_number()
number3 = random_number()

while number1 != number2 or number2 != number3 or number3 != number1 :
    number1 = random_number()
    number2 = random_number()
    number3 = random_number()

    print(f"{number1} - {number2} - {number3}")