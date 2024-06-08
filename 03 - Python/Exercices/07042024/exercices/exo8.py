"""
#! énoncé
Écrivez un script qui demande à l'utilisateur un mot de passe.
Si le mot de passe entré n'est pas "Pyth0n" le programme demande à nouveau
le mot de passe.
Quand le mot de passe est bon, le programme affiche "Mot de passe valide."
Après 3 tentatives infructueuses, le programme affiche "Mot de passe
incorrect."

#! décripteur Belynn1312
#? Instancier une variable qui va contenir une chaîne de caractères
#? Demander une chaîne de caractères à entrer par l'user qui sera injectée dans la variable instanciée
#? Initialiser un bloc d'instruction CONDITION
#?      SI le mot de passe entré n'est pas "Pyth0n"
#?          Redemander le mot de passe
#?      QUAND le mot de passe est bon
#?          Afficher la chaîne de caractères "Mot de passe valide."
#? Initiatliser un compteur
#?      APRES 3 tentatives
#?          Afficher la chaîne de caractères "Mot de passe incorrect."
"""

text = None
count = 3

# Bloc d'instruction BOUCLE TANT QUE
while text != "Pyth0n" and count > 0 :
    # Bloc d'instruction CONDITION
    text = input("Mot de passe : ")
    count -= 1

if count == 0 and text != "Pyth0n" :
    print("Mot de passe incorrect.")
else :
    print("Mot de passe valide.")