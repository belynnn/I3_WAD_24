""" # ! Énnoncé 
Récupérez un nombre au clavier et stockez-le dans une variable.
Si le nombre récupéré est plus grand ou égale à 10 affichez “Bravo!”.
Sinon, si il est plus grand que 8 affichez “Pas mal.”
Sinon, si le nombre est plus grand que 5 affichez “Mouais, bof”
Et sinon dans les autres cas affichez “Pas terrible”
# ? demander un nombre et affecter la valeur à une variable
# ? condition si le nombre affecté à la valeur est plus grand ou égal à 10
# ? affiche le message "Bravo!"
# ? si la première condition n'est pas remplie, condition si le nombre affecté à la valeur est plus grand que 8 :
# ? afficher le message "Pas mal."
# ? si la seconde condition n'est pas remplie, condition si la nombre affecté à la valeur est plus grand que 5 :
# ? afficher le message "Mouais, bof"
# ? si toute les conditions ne sont pas remplie
# ? afficher le message "Pas terrible"
"""

number = int(input("Entrez un nombre : "))

if number >= 10 :
    print("Bravo!")
elif number > 8 :
    print("Pas mal.")
elif number > 5 :
    print("Mouais, bof")
else :
    print("Pas terrible")