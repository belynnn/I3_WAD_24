"""
#! énoncé
Générez deux nombres aléatoire (entre 0 et 100)
Affichez ces deux nombres en demandant à l'utilisateur d'en donner la
somme
Continuez à lui demander tant que la réponse est mauvaise.
A la fin du programme, affichez à l'utilisateur le nombre d'erreurs qu'il a commises.

#! décripteur Belynn1312
#? Instancier 2 variables contenant une valeur numérique aléatoire
#? Injectée 1 nombre aléatoire entre 1 et 100
#? Instancier 1 variable contenant la somme des 2 première variables
#? Instancier 1 compteur commençant à 0
#? Instancier 1 variable contenant int pour stocker la valeur de l'user après
#? Initialiser 1 bloc d'instruction BOUCLE TANT QUE
#?      TANT QUE la valeur entrée par l'user EST DIFFERENTE de la somme des 2 variables
#?          Redemander d'entrer la somme
#?          Ajouter 1 au compteur
#?          Initialiser 1 bloc d'instruction CONDITION
#?              SI la valeur entrée pas l'user EST EGALE à la somme des 2 variables
#?                  Afficher le nombre de tentatives
"""

from random import randint

def random_number() :
    number = randint(1,10)

    return number

number1 = random_number()
number2 = random_number()
sum = number1 + number2
count = 0
user_entry = int

while user_entry != sum :
    user_entry = int(input(f"Somme de {number1} et {number2} : "))
    count += 1

    if user_entry == sum :
        print(f"Vous avez réalisé {count} tentatives.")