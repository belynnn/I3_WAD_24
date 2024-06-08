
























# """ # ! Ennoncé
# 1. Générer le code à deviner
# 2. Demander une tentative de décodage au joueur
# 3. Vérifier quelles lettres proposées par le joueur sont correctes
# 4. Mettre le tout dans une boucle
# 5. Gérer les lettres mal placées
# 6. Gérer le nombre de tentatives et afficher un message de victoire/défaite
# """
# from random import randint

# # ? Affectations relative à la génération du code + reste
# letters = ["a", "b", "c", "d", "e", "f"]
# code = []
# len_code = 4 # slide128 # à n'utiliser que pour la génération de code

# # ? Génération aléatoire du code à découvrir
# for letter in range(len_code) :
#     letter = randint(0, len(letters)-1)
#     code.append(letters[letter])
# code = ["a", "b", "a", "d"] # code forcé pour debug
# print(f"\n\n  ->  CODE : {code}") # ! code généré

# # ? Affectations relatives au while + reste
# count = 5
# answer = ""
# wrong_index = []
# correct_index = []

# # ? Tant que différent de code et que longueur différent
# while answer != code or len(answer) != len(code) :
#     answer = input("Entrez 4 lettres : ")
#     answer = list(answer)
#     print(f"  -> ANSWER  : {answer}")

#     # ? FOR : Si, au même index, la réponse est == au code : append index correct
#     for i_answer in range(len(answer)) :
#         # print(len(code)) - utilisé en debug
#         for i_code in range(len(code)) :
#             # print("code str") - utilisé en debug
#             if answer[i_answer] == code[i_code] :
#                 correct_index.append(i_answer)

#                 if code[i_code] not in correct_index and answer[i_answer] not in correct_index and code[i_code] not in wrong_index :
#                     wrong_index.append(i_code)
#                     break

#     print(f"  -> CORRECT : {correct_index}") # à changer par len(correct_index) à la fin
#     print(f"  -> WRONG   : {wrong_index}") # à changer par len(wrong_index) à la fin

#     if answer == code :
#         print("Waa t'es trop fort!")


# COMPTEUR
# while count < len(count) :
#     count -= 1



    # for i_answer in range(len(answer)) :
    #     for i_code in range(len(code)) :
    #         # ! Si l'un des deux index est dans notre liste d'index corrects, la lettre a déjà été "traitée", et il faut ignorer la combinaison
    #         if answer[i_answer] in correct_index or code[i_code] in correct_index :
    #             break
    #         # ! Si l'index du code correspond à une lettre mal placée 'identifiée auparavant', il faut aussi ignorer cet index
    #         elif code[i_code] not in wrong_index :
    #             print(code[i_code])
    #             wrong_index.append(i_code)
    #         # !
    #         elif code[i_code] in wrong_index :
    #             break
    #         # ! Sinon, si la lettre du code et de la proposition sont égales, il faut s'arrêter de chercher, et stocker l'index du code comme "mal placé"
    #         elif code[i_code] == answer[i_answer] :
    #             correct_index.append(i_code)



    # for index in range(len(answer)) :
    #     if answer[index] == code[index] :
    #         correct_index.append(index)
    #     elif answer[index] in code and answer[index] != code[index] :
    #         wrong_index.append(index)
    #     else :
    #         no_index.append(index)



# # ? Affectations
# letters = ["a", "b", "c", "d", "e", "f"]
# code = ["a", "a", "c", "d"]
# len_code = 4 # slide128
# attempt = ""
# correct_index = []
# wrong_index = []

# # # ? génération aléatoire du code à découvrir
# # for letter in range(len_code) :
# #     letter = randint(0, len(letter_list)-1)
# #     code.append(letter_list[letter])
# print(f"\n\n  ->  CODE : {code}") # ! code généré - à supprimer plus tard

# print("\n************************************************")
# print("***                MASTERMIND                ***")
# print("************************************************\n")
# print("Essayez de deviner le code de 4 lettres parmis :")
# print(f"  ->  LISTE : {letters}\n")

# while len(attempt) != len(code) :
#     attempt = input("Votre proposition (x essai(s) restant): ")

# for i in range(len(attempt)) :
#     if attempt[i] == code[i] :
#         correct_index.append(i)
#     elif attempt[i] != code[i] :
#         wrong_index.append(i)
#     else :
#         print("pas bon")

# print(f"  ->  CORRECT : {correct_index}")
# print(f"  ->    WRONG : {wrong_index}")



# letters = ["a", "b", "c", "d", "e", "f"]
# code = []
# result = []
# len_max_code = 4
# user_letter_placed = 0
# user_letter_misplaced = 0

# for i in range(len_max_code) :
#     i = randint(0,len(letters) - 1)
#     code.append(letters[i])

# print(code)
# print(f"Essayez de deviner le code de 4 lettres parmis : \n{letters}")
# user_attempt = input("Votre proposition : ")

# while len(user_attempt) < len(code) or len(user_attempt) > len(code) :
#     user_attempt = input("Votre proposition : ")

# if len(user_attempt) == len(code) :
#     user_answer = list(user_attempt)
    
#     print(f"Vous avez entrez : \n{user_answer}")

# for i in range(len_max_code) :
#     if user_answer[i] == code[i] :
#         result.append(user_attempt[i])

#         user_letter_placed += 1
#     else :
#         user_letter_misplaced += 1

# print(f"Vous avez trouvé {user_letter_placed} lettre(s).")
# print(f"Vous avez trouvé {user_letter_misplaced} lettre(s) mais elles sont mal placée(s)")
# print(result)



# if user_answer[i] in code :
#     print(f"Vous avez trouvé {i} lettre(s).")

# """
# 0 1 2 3
# c b d a
# a b c d

# index = 0
# """
    


# for i in range(len_max_code) :
#     if code[i] == user_attempt[i] :
#         print(f"Vous avez trouvé la lettre à l'index {i}.")
#         result.append(user_attempt[i])
#     elif user_attempt[i] != code[i] and user_attempt[i] in code :
#         print(f"Vous avez une lettre trouvée mais mal placée à l'index {i}.")



# slide 146
# # Ennoncé
# """
# [v] Demander d'entrer une proposition de la même longueur que le code
# [v] Valider la longueur de la proposition donnée par le joueur
# [v] Redemander une si cette longueur n'est pas correcte
# [v] Transformer la proposition du joueur en liste de lettres en utilisant list()
# """
# from random import randint

# # AFFECTATIONS
# letters = ["a", "b", "c", "d", "e", "f"]
# code = []
# len_max_code = 4

# # BOUCLE pour chaque index dans la range de la longueur du code souhaité
# for i in range(len_max_code) :
#     i = randint(0,len(letters) - 1)
#     code.append(letters[i])

# print(code)

# user_attempt = input("Entrez la bonne combinaison (4 lettres) : ")

# while len(user_attempt) < len(code) or len(user_attempt) > len(code) :
#     user_attempt = input("Veuillez entrez 4 lettres : ")

# if len(user_attempt) == len(code) :
#     user_answer = list(user_attempt)
#     print(f"Vous avez entrez : \n{user_answer}")


# slide 147
# # Ennoncé
# """
# [x] Essayez de remplacer la boucle while par une boucle for
# """

# from random import randint

# letters = ["a", "b", "c", "d", "e", "f"]

# code = []
# len_max_code = 4

# for i in range(len_max_code) :
#     i = randint(0,len(letters))
#     code.append(letters[i])

# print(code)



# # Ennoncé
# """
# [v] Création d'une liste vide dans une variable code
# [v] Boucle while tant que quatre lettres n'ont pas été choisies:
#     [v] Sélection d'un index au hasard de la liste de lettres à l'aide de randint()
#     [v] Ajout de la lettre choisie dans la liste code
# [v] Affichage du code final (pour tester)
# """

# from random import randint

# letters = ["a", "b", "c", "d", "e", "f"]

# code = []
# len_max_code = 4

# while len(code) < len_max_code :
#     i = randint(0,len(letters) - 1)
#     code.append(letters[i])

# print(code)