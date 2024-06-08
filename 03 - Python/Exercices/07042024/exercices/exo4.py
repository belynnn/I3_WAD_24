"""
#! énoncé
Dans le même script :

Si le nombre qui se trouve dans la variable number est plus grand que 10, affichez la chaîne de caractères "Ce nombre est plus grand que 10"

#! décripteur Belynn1312
#? Reprendre le script initial
#? Modifier la variable "user_entry" par "number", variable qui...
#? récupère la valeur entrée par l'utilisateur
#? variable qui doit être convertie en nombre entier
#? Initialiser un bloc d'instruction de condition :
#?     Si le nombre entré par l'utilisateur est PLUS GRAND que 10
#?         Afficher la chaîne de caractères "Ce nombre est plus grand que 10"
"""

number = input("Entrez un nombre : ")
number = int(number)

# OU
# user_entry = int(input("Entrez un nombre : "))

# Bloc d'instruction CONDITION
if number > 10 :
    print("Ce nombre est plus grand que 10")