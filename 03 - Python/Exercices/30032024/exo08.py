""" # ! Énnoncé  
Écrivez un script qui demande à l'utilisateur un mot de passe.
Si le mot de passe entré n'est pas "Pyth0n" le programme demande à nouveau
le mot de passe.
Quand le mot de passe est bon, le programme affiche "Mot de passe valide."
Après 3 tentatives infructueuses, le programme affiche "Mot de passe incorrect."
# ? instancier une variable 'correct_password' avec pour valeur définie 'Pyth0n'
# ? utiliser un compteur pour gérer les essais et instancier une variable 'count' avec pour valeur définie '0'
# ? instancier une variable 'count_max' avec pour valeur définie '3' car trois tentatives maximum
# ? instancier une variable 'password' avec pour valeur définie 'None'
    # ! cela permet de bien comptabiliser 0>1 un essai, 1>2 deux essais, 2>3 trois essais
    # ! si l'on demandait directement d'entrer une valeur AVANT la déclaration de la boucle TANT QUE, il faut déclarer la valeur de la variable 'count_max' à '2', car cela comptabilise 0 un essai, 0>1 deux essais, 1>2 trois essais
# ? déclarer boucle TANT QUE la valeur définie de la variable 'count' est plus petit que la valeur définie de la variable 'count_max' ET que la valeur affectée de la variable 'password' est différente de la valeur définie à la variable 'correct_password', redemander à l'user, une valeur à affecter à la variable 'password'
# ? dans cette boucle déclarée TANT QUE, incrémenter la valeur définie de la variable 'count' de '1'
# ? fin de boucle, déclarer condition SI la valeur définie et/ou incrémentée de la variable 'count' est égale à la valeur définie de la variable 'count_max' ET que la valeur affectée par l'user de la variable 'password' est différente de la valeur définie de la variable 'correct_password', afficher le message "Mot de passe incorrect.", SINON, afficher le message "Mot de passe valide."
"""

correct_password = "Pyth0n"
count = 0
count_max = 3

password = None

while count < count_max and password != correct_password :
    password = input("Entrez le bon mot de passe : ")

    count += 1

if count == count_max and password != correct_password:
    print("Mot de passe incorrect.")
else :
    print("Mot de passe valide.")