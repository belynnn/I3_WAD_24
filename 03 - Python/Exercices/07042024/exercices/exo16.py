"""
#! énoncé
Créez un script qui demande à l'utilisateur un mot.
Ensuite donner à l'utilisateur le nombre de voyelle de ce mot.
Indice: vous pouvez établir la liste des voyelles facilement ["a", "e", "i", "o", "u", "y"] et nous avons vu un moyen de vérifier qu'un élément se trouve dans un groupe.

#! décripteur Belynn1312

"""

vowels = ["a", "e", "i", "o", "u", "y"]

word = input("Mot : ")
count = 0

for vowel in word :
    if vowel in vowels :
        count += 1

print(count)