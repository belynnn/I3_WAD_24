""" # ! Énnoncé  
Écrivez un programme qui va générer trois nombres aléatoirement (entre 1 et 6).
Ensuite le programme va afficher les trois nombres
Si les trois nombres ne sont pas identiques, il recommence.
# ? importer la fonction randint de la librairie random
# ? instancier 3 variables (number1, number2, number3) recevant chacune 1 valeur numérique générée aléatoirement grâce à la fonction randint
# ? déclarer boucle TANT QUE les variables (number1, number2, number3) sont != entre elles, générer aléatoirement 1 valeur numérique grâce à la fonction randint affectée à leurs variables respectives
# ? afficher les numéros générés aléatoirement (dans la boucle)
# ? fin de boucle, quand la condition est remplie (TANT QUE les variables sont différentes entre elles, SI elles sont finalement égales entre elles), afficher les derniers nombres générés aléatoirement qui ont une valeur identique
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