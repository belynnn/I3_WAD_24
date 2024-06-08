"""
#! énoncé
Dans un autre script :

Récupérez au clavier un nombre et stockez-le dans une variable
Ensuite, afficher cette variable
Rappelez-vous, la saisie clavier revient sous forme de chaîne de caractères.

#! décripteur Belynn1312
#? Initialiser une variable qui va...
#? récupérer un nombre demander à l'utilisateur, pour...
#? afficher la valeur stockée dans la variable, valeur qui...
#? doit être convertie en chaîne de caractères
"""

user_entry = input("Entrez un nombre : ")
user_entry = int(user_entry)

# OU
# user_entry = int(input("Entrez un nombre : "))

print(str(user_entry))