"""
Demander au joueur d'essayer de deviner le code
    -> INPUT string, on attend des lettres
La longueur de la tentative du joueur ne doit pas être plus petite ou plus grande que la longueur du code généré
    - SI True, redemander une tentative
    - quand condition remplie, passe à la suite
# ! GENERATION DU CODE ALEATOIRE
    # ? création d'une liste vide dans une variable code
    # ? création d'une boucle while indiquant que si la longueur du code est plus petite que la longueur du code définie plus haut
        # * 
    # ? afficher le code généré pour le tester
# ! SLIDE 153
    # ? création d'une boucle for qui, avec la fonction range() va parcourir une séquence de chiffre de la longueur du code, dont la valeur est contenue dans la constante CODE_LENGHT
        # * à chaque itération, utilisation d'une condition indiquant que si l'index de guess_list est égale à l'index de code (ici l'index étant indiquée par i, par chaque itération)
            # * si TRUE -> ajoute le numéro de l'itération à la liste gérant les index qui sont égaux (correct_index)
    # ? i pour itération
"""

from random import randint

CODE_LENGHT = 4
COUNT = 15
LETTERS = ["a", "b", "c", "d", "e", "f"]
code = []

# GENERATION DU CODE ALEATOIRE
# while len(code) < CODE_LENGHT :
#     index = randint(0, len(LETTERS) - 1)

#     letter = LETTERS[index]

#     code.append(LETTERS[index])

# SLIDE 147
for _ in range(CODE_LENGHT) :
    index = randint(0, len(LETTERS) - 1)

    letter = LETTERS[index]

    code.append(letter)

guess = ""

for i in range(COUNT) :
    while guess != code :
        # SLIDE 149
        while len(guess) != len(code) :
            guess = input(f"\nEntrez {CODE_LENGHT} lettres : ")

            # En python on pourrait remettre guess = list(guess) ou écrire directement guess = list(input("blablabla")), mais cette façon de faire n'existe pas en C#
            guess_list = list(guess)

        # SLIDE 153 - confirmer les lettres exactes
        # remettre les listes à 0 pour retraiter l'égalité
        correct_index = []
        wrong_index = []
        for i_guess in range(CODE_LENGHT) :
            if guess_list[i_guess] == code[i_guess] :
                correct_index.append(i_guess)

        # SLIDE 157 - comptabiliser les lettres correctes mais mal placées
        # pour chaque lettre du user, on passe par chaque lettre du code
        # Vérification des lettres mal placées
            # pour l'itération 0 de l'index de guess :
            #   pour l'itération 0 de l'index de code :
            #       condition
            #   pour l'itération 1 de l'index de code :
            #       condition
            #   pour l'itération 2 de l'index de code :
            #       condition
            #   pour l'itération 3 de l'index de code :
            #       condition
            # pour l'itération 1 de l'index de guess :
            #   pour l'itération 0 de l'index de code :
            #       condition
            #   pour l'itération 1 de l'index de code :
            #       condition
            #   pour l'itération 2 de l'index de code :
            #       condition
            #   pour l'itération 3 de l'index de code :
            #       condition
        for i_guess in range(CODE_LENGHT) :
            for i_code in range(CODE_LENGHT) : # boucle + rapidement que la boucle parente
                # j'avais mis guess_list[i_guess] == code[i_guess] car je gardais en tête le fait de valider 2 même valeurs à 2 même index, or ici, on souhaite savoir si, lors de l'itération de la boucle i_guess, à cette itération de la séquence de la boucle i_code
                if guess_list[i_guess] == code[i_code] :
                    if i_code not in correct_index and i_guess not in correct_index and i_code not in wrong_index :
                        wrong_index.append(i_code) # j'avais mis wrong_index.append(i_guess) alors qu'actuellement, on est en train d'itérer sur la séquence de i_code
                        break

        # RESULTATS
        print(f"\t-> CODE    : {code}")
        print(f"\t-> REPONSE : {guess_list}")
        print(f"\t-> CORRECT : {correct_index}")
        print(f"\t-> WRONG   : {wrong_index}\n")
        print(f"Vous avez trouvé {len(correct_index)} lettre(s).")

        # redemander un essai à l'utilisateur en diminuant le nombre d'essai à chaque tour de boucle
        guess = input(f"\n-> Entrez 4 lettres ({COUNT - 1} essai(s)) : ")
        guess_list = list(guess)