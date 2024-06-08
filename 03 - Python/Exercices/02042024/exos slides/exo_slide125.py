# Ennoncé
""" 
[v] Créez une liste contenant 5 nombres de 1 à 5.
[v] Affichez la liste.
[v] Tant que la liste n'est pas vide (ex: tant que sa longueur est > 0):
[v] Retirez le premier élément de la liste
[v] Affichez l'élément retiré de la liste
[v] Affichez la liste
"""

number_list = [1, 2, 4, 5, 1]

print(number_list)

while len(number_list) > 0 :
    removed = number_list.pop(0)
    print(removed)
    print(number_list)



####################################
# CORRECTION                       #
####################################

# same résultat que la correction