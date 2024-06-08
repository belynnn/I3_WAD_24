"""
#! énoncé
Dans le même script :

A la suite de la condition, si celle-ci n'est pas remplie, afficher le message suivant : "Le nombre est plus petit ou égal à 10."

#! décripteur Belynn1312
#? Reprendre le script initial
#? Ajouter dans le bloc d'instruction de condition :
#?     Si la première condition n'est pas remplie
#?         Afficher la chaîne de caractères "Le nombre est plus petit ou égal à 10"
"""

number = input("Entrez un nombre : ")
number = int(number)

# OU
# user_entry = int(input("Entrez un nombre : "))

# Bloc d'instruction CONDITION
if number > 10 :
    print("Ce nombre est plus grand que 10")
else :
    print("Le nombre est plus petit ou égal à 10.")