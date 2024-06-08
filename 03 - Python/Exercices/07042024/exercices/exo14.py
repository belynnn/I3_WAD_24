"""
#! énoncé
Écrivez un script qui demande un mot à l'utilisateur.
Tant que le mot n'est pas "end" le script redemandera un mot à l'utilisateur.
A chaque fois que le mot commence par "t", affichez-le suivi de "!!!" (rappelez-vous que pour lire un seul caractère d'une chaîne de caractères, on doit lui donner son index (comme pour les listes)).
A la fin du script, affichez le nombre de mots entrés par l'utilisateur.

#! décripteur Belynn1312
#? Instancier une variable ayant pour valeur une chaîne de caractère
#? Demander à l'user d'entrer une chaîne de caractère
#? Initialiser un bloc d'instruction BOUCLE TANT QUE
#?      TANT QUE le mot entré par l'user N'EST PAS "end"
#?          Redemander d'entrer une chaîne de caractère
#?          Initialiser un bloc d'instruction CONDITION
#?              SI la 1ère lettre à l'index 0 du mot est EGALE à "t"
#?                  Afficher le mot suivi de "!!!"
#?      QUAND condition remplie
#?          Afficher le total de chaîne de caractères entrés
#! "end" ne doit pas être compris
"""

word = None
total_word = 0
while word != "end" :
    word = input("Mot ('end' pour terminer) : ")
    total_word += 1

    if word[0] == "t" :
        print(f"{word}!!!")

    if word == "end" :
        total_word -= 1
        print(f"Total de mots entrés : {total_word}")