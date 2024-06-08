# Énnoncé
"""
[v] ● Écrivez un script qui demande à l'utilisateur un mot de passe.
[v] ● Si le mot de passe entré n'est pas "Pyth0n" le programme demande à nouveau le mot de passe.
[v] ● Quand le mot de passe est bon, le programme affiche "Mot de passe valide."
[v] ● Après 3 tentatives infructueuses, le programme affiche "Mot de passe incorrect."
# ! réalisé en 15min
"""

# 1) affecte None à la variable password
password = None
# 2) affecte "Pyth0n" à la variable ' correct password '
correct_password = "Pyth0n"

# 3) compteur d'essai à 0
attempt = 0
# 4) maximum d'essai possible
max_attempt = 3

# 5) tant que le compteur d'essai est plus petit que le maximum d'essai possible ET que le password est != de correct password
while attempt < max_attempt and password != correct_password :
    # 6) affecter l'entré de l'user à la variable ' password '
    password = input("Entrez le bon mot de passe : ")

    # 8) si ' password ' est égal OU que le compteur d'essai est égal au maximum d'essai possible
    if password == correct_password or attempt == max_attempt :
        # 9) print message
        print("Mot de passe valide.")
    else :
        # 7) ajoute 1 au compteur d'essai (0 devient 1)
        attempt += 1

# ! fin de la boucle

# 10) si 'password' est != de 'correct password'
if password != correct_password :
    # 11) print message
    print("Mot de passe incorrect.")



# !  DOROTHEE
# password = None
# correct_password = "Pyth0n"

# attempt = 0
# max_attempt = 3

# while attempt < max_attempt and password != correct_password :
#     password = input("Entrez le bon mot de passe : ")

#     attempt += 1

#     if password == correct_password :
#         print("Mot de passe valide.")

# if attempt == max_attempt :
#     print("Mot de passe incorrect.")