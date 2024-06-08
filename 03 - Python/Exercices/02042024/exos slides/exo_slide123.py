# Ennoncé
"""
[v] Créez une liste contenant 10 nombres de 1 à 5.
[v] Affichez la liste.
[v] Demandez à l'utilisateur d'entrer un nombre au clavier.
[v] Retirez le nombre entré de la liste.
[v] Affichez la liste finale.
"""

number_list = [5, 2, 8, 4, 0, 5, 4, 6, 2, 1]

print(number_list)

user_number = int(input("Entrez un nombre entre 1 et 5 : "))

number_list.remove(user_number)

print(number_list)



####################################
# CORRECTION                       #
####################################
# numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

# print(numbers)

# number = int(input("Nombre : "))

# numbers.remove(number)

# print(numbers)