""" # ! Énnoncé 
Demandez à l'utilisateur d'entrer des nombre jusqu'à ce qu'il donne la valeur 0.
Ensuite, affichez le plus grand et le plus petit nombre que l'utilisateur a donné.
# ? instancier une variable 'correct_number' ayant pour valeur définie '0', car on attend que l'user entre '0' pour finir le programme
# ? demander à l'user d'entrer une valeur numérique qui sera affectée à la variable 'user_number' qui sera comparée à aux différents nombres (autre que '0'), entrés par l'user
# ? instancier une variable 'compare' qui va être affectée par le nombre entré par l'user
# ? instancier une variable 'little' qui va être affectée par la variable 'compare'
# ? instancier une variable 'big' qui va être affectée par la variable 'little'
    # ! l'user entre 4, 4 devient 'user_number', 4 devient 'compare', 4 devient 'little', 4 devient 'big'
    # ! boucle TANT QUE 4 est différent de '0', si 4 est plus petit que 4, 4 devient 'little', si 4 est plus grand que 4, 4 devient 'big'
    # ! redemander d'entrer un nombre car '0' n'a pas été entré, l'user entre 8
    # ! boucle TANT QUE 8 est différent de '0', si 8 est plus petit que 4, ce n'est pas le cas, condition suivante, si 8 est plus grand que 4, 8 devient 'big', ETC
# ? déclarer une boucle TANT QUE la valeur affectée à la variable 'user_number'
# ? fin de boucle, condition SI la valeur de la variable 'user_number' est égale à la valeur de la variable 'correct_number', afficher le plus petit et le plus grand nombre entré par l'user
"""

correct_number = 0

user_number = int(input("Entrez un nombre : "))

compare = user_number
little = compare
big = little

while user_number != correct_number :
    user_number = int(input("Entrez un nombre : "))

    if user_number < compare :
        little = user_number
    elif user_number > compare :
        big = user_number

if user_number == correct_number :
    print(f"Petit : {little}")
    print(f"Grand : {big}")



####################################
# CORRECTION                       #
####################################
# number = int(input("Nombre : "))

# greater = number
# lower = number

# while number != 0 :
#     number = int(input("Nombre : "))

#     if number < lower :
#         lower = number
#     elif number > greater :
#         greater = number

# print(f"Petit : {lower}")
# print(f"Grand : {greater}")