"""
#! énoncé
Mettre la valeur 10 dans une variable
Utilisez une boucle while pour afficher les nombres de 10 à 1.
Terminez en affichant "Décollage !"

#! décripteur Belynn1312
#? Instancier une variable ayant pour valeur numérique 10
#? Initialiser un bloc d'instruction BOUCLE TANT QUE
#?      TANT QUE la valeur 10 de la variable PLUS GRANDE que 1
#?          Afficher -1 à chaque boucle jusqu'à 1
#?          Afficher "Décollage" quand compteur à 1
"""

number = 10

while number > 0:
    print(number)
    number -= 1

    if number == 0 :
        print("Décollage !")