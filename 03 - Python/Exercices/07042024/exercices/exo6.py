""" 
#! énoncé
Dans un autre script :

Récupérez un nombre au clavier et stockez-le dans une variable
Si le nombre récupéré est plus grand ou égal à 10 affichez "Bravo!"
Sinon, si il est plus grand que 8 affichez "Pas mal."
Sinon si le nombre est plus grand que 5 affichez "Mouais, bof"
Et sinon dans les autres cas affichez "Pas terrible"

#! décripteur Belynn1312
#? Instancier une variable va contenir une valeur numérique
#? Récupèrer une valeur numérique entrée par l'user, qui est stockée dans la variable qui a été instanciée
#? Variable ou valeur qui doit être convertie en nombre entier
#? Initialiser un bloc d'instruction de CONDITION
#?     SI le nombre de l'utilisateurice est PLUS GRAND OU EGAL à 10
#?         Afficher "Bravo!!!"
#?     SINON, si le nombre est PLUS GRAND que 8
#?         Afficher "Pas mal!"
#?     SINON, si le nombre est PLUS GRAND que 5
#?         Afficher "Mouais, bof..."
#?     ETSINON, dans les autres cas
#?         Afficher "Pas terrible."
"""

number = int(input("Entrez un nombre : "))

if number >= 10 :
    print('Bravo!!!')
elif number > 8 :
    print("Pas mal!")
elif number > 5 :
    print("Mouais, bof...")
else :
    print("Pas terrible.")