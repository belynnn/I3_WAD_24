""" # ! Énnoncé 
Stockez dans une variable le résultat d'une saisie au clavier et affichez-la.
Une saisie au clavier est ce que l'utilisateur a écrit sur le clavier (avant d'appuyer sur “enter”)
A la place d'afficher simplement la variable, affichez son contenu précédé de la
chaîne de caractères “Saisie clavier: ”.
# ? création d'une variable 'text'
# ? affectation d'une valeur saisie au clavier à la variable 'text'
# ? afficher la valeur saisie affectée à la valeur 'text' dans le prompt
# ? afficher "Saisie clavier: " suivi de la variable
"""

text = None
text = input("Entrez un mot : ")

print(text)
print("Saisie clavier: " + text)