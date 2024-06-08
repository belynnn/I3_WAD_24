"""
#! énoncé
Écrivez un script qui demande à l'utilisateur un nombre entier entre 1 et 100, redemandez tant que l'utilisateur ne donne pas un entier entre 1 et 100.
Ensuite affichez la somme des chiffres de 1 à l'entier donné par l'utilisateur.
Si l'utilisateur vous donne 10, la somme affichée sera 55 car 55 est la somme des entiers de 1 à 10.

#! décripteur Belynn1312
#? Instancier une variable qui comprendre une valeur numérique
#? Demander à l'user d'entrer un nombre entre 1 et 100
#? Initialisation d'un bloc d'instruction BOUCLE TANT QUE
#?      TANT QUE le nombre entré par l'user est PLUS PETIT que 1 OU PLUS GRAND que 100
#?          Redemander d'entrer un nombre
#?      QUAND condition remplie
#?          Afficher la somme des nombres entré de 1 au nombre entré par l'user (s'il donne 10, print doit afficher 55)
"""

number = int(input("Nombre entre 1 et 100 : "))
sum = 0

while number < 1 or number > 100 :
    number = int(input("Nombre entre 1 et 100 : "))

for n in range(number+1) :
    sum += n

print(sum)