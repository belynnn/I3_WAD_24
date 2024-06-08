""" # ! Énnoncé 
Générez deux nombres aléatoire (entre 0 et 100)
Affichez ces deux nombres en demandant à l'utilisateur d'en donner la somme
Continuez à lui demander tant que la réponse est mauvaise.
A la fin du programme, affichez à l'utilisateur le nombre d'erreurs qu'il a commises.
# ? importer la fonction 'randint' de la librairie 'random'
# ? instancier 2 variables (number1 et number2) qui seront affectées par une variable numérique générée aléatoirement entre 0 et 100
# ? créer un compteur et instancer une variable 'count' ayant pour valeur définie '0'
# ? instancier la variable 'sum' avec pour valeur la somme des valeurs numérique générées aléatoirement des variables 'number1' et 'number2'
# ? afficher les valeurs générées aléatoirement des 2 variables et demander à l'user d'entrer la somme de ces 2 valeurs numériques, la somme entrée par l'utilisateur est affectée à une variable 'user_number'
# ? boucle TANT QUE l'user n'a pas entré la somme correcte des 2 valeurs numérique, continuer la boucle
# ? incrémenter la valeur de la variable 'count' de '1' à chaque tour pour comptabiliser le nombre d'erreur commise par l'user
# ? fin de boucle, si la condition est remplie, afficher le nombre d'erreurs commis par l'user
"""

from random import randint

number1 = randint(1, 99)
number2 = randint(1, 99)

count = 0

sum = number1 + number2

user_number = int(input(f"Entrez la somme de {number1} et {number2} : "))

while user_number != sum :
    user_number = int(input(f"Entrez la somme de {number1} et {number2} : "))

    count += 1

print(f"Vous avez entré {count} réponses éronnées.")



####################################
# CORRECTION                       #
####################################
# from random import randint

# n1 = randint(1, 99)
# n2 = randint(1, 99)

# errors = 0
# answer = int(input(f"Entrez la somme de {n1} et {n2} : "))

# while answer != (n1 + n2) :
#     errors += 1
#     answer = int(input(f"Entrez la somme de {n1} et {n2} : "))

# print(f"Vous avez entré {count} réponses éronnées.")