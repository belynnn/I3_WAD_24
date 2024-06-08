""" # ! Énnoncé 
Écrivez un script qui demande un mot à l'utilisateur.
Tant que le mot n'est pas "end" le script redemandera un mot à l'utilisateur.
A chaque fois que le mot commence par "t", affichez-le suivi de "!!!" (rappelez-vous que pour lire un seul caractère d'une chaîne de caractères, on doit lui donner son index (comme pour les listes)).
A la fin du script, affichez le nombre de mots entrés par l'utilisateur.
# ? instancier la variable 'text' qui sera affectée par la valeur 'None' afin de pouvoir l'utiliser dans une boucle ou une condition (bloc d'instruction)
# ? instancier la variable 'correct_text' affectée par la valeur définie 'end'
# ? instancier la variable 'value_to_search' affectée par la valeur définie 't'
# ? créer un compteur, instancier la variable 'count' affectée par la valeur définie '0'
# ? déclarer boucle TANT QUE la valeur de la variable 'text' est différente de la valeur définie de la variable 'correct_text', demander d'entrer des mots à l'user
# ? condition SI la valeur de la variable 'text' a pour premier caractère (indice 0), la valeur définie 't' de la variable 'value_to_search', afficher ce mot suivi de "!!!" et incrémenter la valeur définie de la variable 'count' de '1'
# ? fin de boucle, afficher le nombre de mots que l'user a entré avec le message "Vous avez entré x mots." (x = count)
"""

# text = None
# correct_text = "end"
# value_to_search = "t"
# count = 0

# while text != correct_text :
#     text = input("Entrez un mot (pour terminer, entrez end) : ")

#     if text[0] == value_to_search :
#         print(f"{text}!!!")

#     if text == correct_text :
#         print(f"-> Vous avez entré {count} mots.")

#     count += 1



####################################
# CORRECTION                       #
####################################
word = input("Entrez un mot (end pour finir) : ")
counter = 1

while word != "end" :
    word = input("Entrez un mot (end pour finir) : ")
    
    if len(word) > 0 and word[0] == "t"  : # vérifie si entrée vide et si la première lettre est "t"
        print(f"{word}!!!")

    counter += 1
print(f"-> Vous avez entré {counter} mots.")