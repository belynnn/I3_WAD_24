# Ennoncé
"""
[v] Faire en sorte que le programme génère aléatoirement un nombre à deviner entre 1 et 10.
[v] Demander à l'utilisateur de donner un nombre entre 1 et 10.
[v] Indiquer à l'utilisateur si son nombre est inférieur, supérieur ou égal au nombre à deviner.
[v] Si la réponse est bonne, le programme s'arrête et félicite le joueur.
[v] Si la réponse est mauvaise le programme reprendra au point 2, 
[v] sauf si c'est la troisième mauvaise réponse, dans ce cas il donnera la bonne réponse à l'utilisateur.

Solution   guess   tries
6          x none  x 0
             5       1
"""
# Importation de la classe " randint ", de la librairie " random "
from random import randint

# Faire en sorte que le programme génère aléatoirement un nombre à deviner entre 1 et 10.
random_number = randint(1,10)

# AFFECTATIONS
attempt = 0
max_attempt = 3

user_number = None

while attempt < max_attempt and user_number != random_number :
    user_number = int(input("Entrez un nombre entre 1 et 10 : "))
    attempt += 1

    if user_number < random_number :
        print("Trop petit !")
    elif user_number > random_number :
        print("Trop grand...")
    else :
        print("OMFG BRAVOOO")

if attempt == max_attempt :
    print(f"La réponse était : {random_number}")




# OLD
"""
# Si la réponse est mauvaise le programme reprendra au point 2
while user_number != random_number :
    # Demander à l'utilisateur de donner un nombre entre 1 et 10.
    user_number = int(input("Entrez un nombre entre 1 et 10 : "))

    # Indiquer à l'utilisateur si son nombre est inférieur, supérieur ou égal au nombre à deviner
    if attempt == max_attempt and user_number != random_number :
        print(f"La réponse était : {random_number}")
        break
    elif user_number < random_number :
        print("Trop petit !")
    elif user_number > random_number :
        print("Trop grand...")
    else :
        print("OMFG")

    attempt += 1
"""

"""
from random import randint

# Demander à l'utilisateur de donner un nombre entre 1 et 10.
user_number = int(input("Entrez un nombre : "))

# Faire en sorte que le programme génère aléatoirement un nombre à deviner entre 1 et 10.
random_number = randint(1,5)

attempt = 0
max_attempt = 2

while attempt < max_attempt :
    # Indiquer à l'utilisateur si son nombre est inférieur, supérieur ou égal au nombre à deviner
    if user_number == random_number :
        break
    
    elif user_number < random_number :
        print("Le nombre est inférieur au numéro généré aléatoirement.")

        attempt += 1
    else :
        print("Le nombre est supérieur au numéro généré aléatoirement.")

        attempt += 1

    # Si la réponse est mauvaise le programme reprendra au point 2
    user_number = int(input("Entrez un nombre : "))

# sauf si c'est la troisième mauvaise réponse, dans ce cas il donnera la bonne réponse à l'utilisateur.
if attempt == max_attempt and user_number != random_number :
    print("La réponse était : " + str(random_number))

# Si la réponse est bonne, le programme s'arrête et félicite le joueur.
else :
    print("Bravo, vous avez trouvé le nombre généré aléatoirement.")
"""