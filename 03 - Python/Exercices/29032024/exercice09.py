# Ennoncé
"""
[v] ● Écrivez un programme qui va générer trois nombres aléatoirement (entre 1 et 6).
[v] ● Ensuite le programme va afficher les trois nombres
[v] ● Si les trois nombres ne sont pas identiques, il recommence.
# ! réalisé en 15min
"""

from random import randint

number1 = randint(1,6)
number2 = randint(1,6)
number3 = randint(1,6)

while number1 != number2 or number2 != number3 or number3 != number1 :
    number1 = randint(1,6)
    number2 = randint(1,6)
    number3 = randint(1,6)

    print(number1, number2, number3)