""" # ! Énnoncé 
Écrivez un script qui demande à l'utilisateur un nombre (entre 1 et 10).
Tant qu'il ne rentre pas un chiffre entre 1 et 10, le programme demande à nouveau à l'utilisateur un nombre (entre 1 et 10).
# ? demander à entrer un nombre (entre 1 et 10) affecté à une variable
# ? créer une boucle "tant que" un nombre est plus petit que 1 OU plus grand que 10
# ? redemande à l'utilisateur d'entrer un nombre (entre 1 et 10)
"""

number = int(input("Entrez un nombre entre 1 et 10: "))

while number < 1 or number > 10 :
    number = int(input("Entrez un nombre entre 1 et 10: "))