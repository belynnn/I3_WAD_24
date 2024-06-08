# Ennoncé
"""
[v] ● Mettre la valeur 10 dans une variable
[v] ● Utilisez une boucle while pour afficher les nombres de 10 à 1.
[v] ● Terminez en affichant "Décollage !"
"""

# # ? Problématique : affiche de 9 à 0
# # affecte la valeur 10 à la variable number
# number = 10

# # tant que 1 est plus petit que number :
# while 0 < number :
#     # number = number -1 (10 = 9)
#     number -= 1 
#     # ? print 9
#     print(number)
#     # ? fin de boucle, si number n'est pas égal à 1, continue la boucle
#     # ? donc si print = 9, prochaine boucle print = 8

# # si number est égal à 1
# if number == 0 :
#     # print décollage
#     print("Décollage !")



# ! Solution
# 1) affecte la valeur 10 à la variable number
number = 10

# 2) tant que 1 est plus petit que number :
while 0 < number :
    # 3) print number (10)
    print(number)
    # 4) number = number -1 (10 = 9)
    number -= 1 
    # ! 5) fin de boucle, si number n'est pas égal à 1, continue la boucle

# 6) si number est égal à 1
if number == 0 :
    # 7) print décollage
    print("Décollage !")