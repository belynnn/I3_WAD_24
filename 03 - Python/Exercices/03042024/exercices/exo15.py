""" # ! Énnoncé 
Écrivez un script qui demande à l'utilisateur un nombre entier entre 1 et 100, redemandez tant que l'utilisateur ne donne pas un entier entre 1 et 100.
Ensuite affichez la somme des chiffres de 1 à l'entier donné par l'utilisateur.
Si l'utilisateur vous donne 10, la somme affichée sera 55 car 55 est la somme des entiers de 1 à 10.
"""

number = int(input("Entrez un nombre entre 1 et 100 : "))
sum = 0

while number < 1 or number > 100 :
    number = int(input("Erreur. Entrez un nombre entre 1 et 100 : "))

for i in range(number+1) :
    sum += i

print(f"  ->  {sum}")



####################################
# CORRECTION                       #
####################################
# number = int(input("entrez un nombre : "))

# while number < 1 or number > 100 :
#     number = int(input("entrez un nombre : "))

# # ! V 1.0
# # somme = 0
# # index = 1

# # while index <= number :
# #     somme += index
# #     index += index

# # V 2.0
# somme = 0

# while number > 0 :
#     somme += number
#     number -= 1

# # V 3.0
# somme = 0
# value = range(number+1)
# somme = sum(value)

# print(somme)