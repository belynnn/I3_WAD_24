""" # ! Énnoncé 
Mettre la valeur 10 dans une variable
Utilisez une boucle while pour afficher les nombres de 10 à 1.
Terminez en affichant "Décollage !"
# ? instancier la variable 'number', affectée par la valeur '10'
# ? créer un compteur et instancier la variable 'count', affectée par la valeur '1'
# ? déclarer boucle TANT QUE la valeur de la variable 'number' est plus grand ou égale à la valeur de la variable 'count', afficher la valeur de la variable 'number' et décrémenter la valeur de la variable 'number' de '1'
# ? condition SI la valeur de la variable 'count' est égale à la valeur de la variable 'number', afficher le message "Décollage !"
"""

# number = 10
# count = 1

# while number >= count : # > 0 ou =! 0 attention !=
#     print(number)

#     number -= 1

# if number == count :
#     print("Décollage !")



####################################
# CORRECTION                       #
####################################
number = 10

while number > 0 :
    print(number)

    number -= 1

print("Décollage !")