"""
#! énoncé
Demandez à l'utilisateur d'entrer des nombre jusqu'à ce qu'il donne la valeur 0.
Ensuite, affichez le plus grand et le plus petit nombre que l'utilisateur a donné.

#! décripteur Belynn1312
#? Instancier une variable qui va contenir une valeur numérique
#? Demander à l'user d'entrer une valeur numérique
#? Initialiser un bloc d'instruction BOUCLE TANT QUE
#?      TANT QUE la valeur entrée par l'user n'est pas 0
#?          Redemander d'entrer une valeur numérique
#?      QUAND condition remplie
#?          Afficher le plus grand et le plus petit nombre que l'user a entré
"""

number = -1
little = number
big = little

while number != 0 :
    number = int(input("Nombre : "))
    
    if number < little :
        little = number
    elif number > big :
        big = number
    
print(f"Petit : {little}\nGrand : {big}")