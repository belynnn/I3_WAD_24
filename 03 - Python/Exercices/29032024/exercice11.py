# Ennoncé
"""
[v] ● Générez deux nombres aléatoire (entre 0 et 100)
[v] ● Affichez ces deux nombres en demandant à l'utilisateur d'en donner la somme
[v] ● Continuez à lui demander tant que la réponse est mauvaise.
[v] ● A la fin du programme, affichez à l'utilisateur le nombre d'erreurs qu'il a commises.
# ! réalisé en 10min
"""

from random import randint

count = 0
number1 = randint(0,100)
number2 = randint(0,100)
print(f"Les deux nombres générés aléatoirement sont :\n{number1}\n{number2}\n")

sum = number1 + number2
# print(f"La somme de ces 2 nombres est : \n{sum}\n")

result = int(input(f"Entrez la somme de {number1} et {number2} : "))

while result != sum :
    result = int(input(f"Erreur. Entrez la somme de {number1} et {number2} : "))

    count += 1

if result == sum :
    print(f"Vous avez entré {count} réponses éronnées.")