"""
#! énoncé
Créez un programme qui va demander à l'utilisateur d'entrer des nombres.
Le programme continuera à en demander tant que l'utilisateur n'aura pas donné deux nombres identiques d'affilée.
En fin de programme, affichez la somme de tous les nombres entrés par
l'utilisateur.

#! décripteur Belynn1312
#? Instancier une variable qui attendra un nombre
#? Demande à l'user d'entrer des valeurs numérique
#? Initialiser un bloc d'instruction BOUCLE TANT QUE
#?      TANT QUE l'user n'aura pas entré 2 x une valeur identique
#?          Redemander d'entrer des valeurs numérique
#?      QUAND condition remplie
#?          Afficher la somme de tous les nombres entrés par l'user
"""

previous = int(input("Nombre : "))
number = int(input("Nombre : "))
sum = number + previous

# Bloc d'instruction BOUCLE TANT QUE
while number != previous :
    previous = number

    number = int(input("Nombre : "))
    
    sum += number

print(sum)