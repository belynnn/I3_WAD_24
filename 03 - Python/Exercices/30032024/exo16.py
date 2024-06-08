""" # ! Énnoncé 
Créez un script qui demande à l'utilisateur un mot.
Ensuite donner à l'utilisateur le nombre de voyelle de ce mot.
Indice: vous pouvez établir la liste des voyelles facilement ["a", "e", "i", "o", "u", "y"] et nous avons vu un moyen de vérifier qu'un élément se trouve dans un groupe.
# ? instancer list 'vowel' regroupant les voyelles
# ? instancer un compteur 'count' ayant pour valeur définie '0'
# ? instancer variable 'text' affectée par la valeur entrée par l'user
# ? déclarer boucle FOR pour chaque indice dans la valeur de la variable 'text', condition SI l'indice est dans la list 'vowel', incrémenter le compteur 'count' de '1'
# ? fin de boucle ? afficher message avec le nombre totale de voyelle dans la valeur de la variable 'text'
"""

vowel = ["a", "e", "i", "o", "u", "y"]
count = 0

text = input("Entrez un mot : ")

for i in text :
    if i in vowel :
        count += 1

print(f"  -> Il y a '{count}' voyelle(s) dans le mot '{text}'")