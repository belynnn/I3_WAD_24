"""
#! énoncé
Écrivez un script qui demande à l'utilisateur un nombre (entre 1 et 10).
Tant qu'il ne rentre pas un chiffre entre 1 et 10, le programme demande à
nouveau à l'utilisateur un nombre (entre 1 et 10).

#! décripteur Belynn1312
#? Instancier une variable qui va contenir une valeur numérique
#? Demander une valeur numérique à entrer par l'user entre 1 et 10 qui sera stockée dans la variable instanciée
#? Variable ou valeur qui doit être convertie en nombre entier
#? Initialiser un bloc d'instruction BOUCLE
#?      TANT QUE l'user n'entre pas un chiffre entre 1 et 10
#?          Continue à demander une valeur numérique entre 1 et 10
"""

number = 0

while number < 1 or number > 10 :
    number = int(input("Entrez un numéro entre 1 et 10 : "))