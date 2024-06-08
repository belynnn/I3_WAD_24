# Énnoncé
"""
[v] Écrivez un script qui demande à l'utilisateur un nombre (entre 1 et 10).
[v] Tant qu'il ne rentre pas un chiffre entre 1 et 10, le programme demande à nouveau à l'utilisateur un nombre (entre 1 et 10).
"""

# Écrivez un script qui demande à l'utilisateur un nombre (entre 1 et 10).
number = int(input("Entrez un nombre entre 1 et 10 : "))

# Tant qu'il ne rentre pas un chiffre entre 1 et 10
while number < 1 or number > 10 :
    # le programme demande à nouveau à l'utilisateur un nombre (entre 1 et 10).
    number = int(input("Entrez un nombre entre 1 et 10 : "))