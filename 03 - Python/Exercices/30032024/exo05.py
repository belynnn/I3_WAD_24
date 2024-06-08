""" 
# ! Énnoncé 
Récupérez au clavier un nombre et stockez-le dans une variable.
Ensuite, affichez cette variable.
Rappelez-vous, la saisie clavier revient sous forme de chaîne de caractères.
Si le nombre qui se trouve dans la variable number est plus grand que 10, affichez la chaîne de caractères “Ce nombre est plus grand que 10”.
A la suite de la condition, si celle-ci n'est pas remplie, affichez le message suivant: “Le nombre est plus petit ou égal à 10.”
# ? demande d'entrer une valeur qui sera affectée à une variable
# ? afficher la variable 'number'
# ? afficher la variable 'number', en chaîne de caractère
# ? si la valeur de la variable 'number' est plus grande que '10'
# ? afficher la variable 'number' en chaîne de caractère "Ce nombre est plus grand que 10"
# ? si la première condition n'est pas remplie
# ? affiche le message "Le nombre est plus petit ou égal à 10."
"""

number = int(input("Entrez un nombre : "))

if number > 10 :
    print("Ce nombre est plus grand que 10")
else :
    print("Le nombre est plus petit ou égal à 10.")



# ! OLD
# number = int(input("Entrez un nombre : "))

# if number > 10 :
#     print("Ce nombre est plus grand que 10")


# # ! OLD
# # number = int(input("Entrez un nombre : "))
# # print(str(number))