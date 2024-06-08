from random import randint

CODE_LENGHT = 4
LETTERS = ["a", "b", "c", "d", "e", "f"]
COUNT_MAX = 12

# Génération du code aléatoire
code = []
for _ in range(CODE_LENGHT) :
    index = randint(0, len(LETTERS) - 1)
    letter = LETTERS[index]
    code.append(letter)

guess = None

count = 0

while guess != code and count < COUNT_MAX :
    print(f"\nNombre d'essai : {COUNT_MAX - count}.")
    count += 1
    guess = input(f"\nEntrez {CODE_LENGHT} lettres : ")
    guess_list = list(guess)

    while len(guess) != len(code) :
        guess = input(f"\nEntrez {CODE_LENGHT} lettres : ")
        guess_list = list(guess)

    correct_index = []
    # Gestion des lettres bien placées
    for i_guess in range(CODE_LENGHT) :
        if guess_list[i_guess] == code[i_guess] :
            correct_index.append(i_guess)

    wrong_index = []
    # Gestion des lettres mal placées
    for i_guess in range(CODE_LENGHT) :
        for i_code in range(CODE_LENGHT) :
            if guess_list[i_guess] == code[i_code] :
                if i_code not in correct_index and i_guess not in correct_index and i_code not in wrong_index :
                    wrong_index.append(i_code)
                    break

    # # ! DEBUG
    # print(f"\t-> CODE    : {code}")
    # print(f"\t-> REPONSE : {guess_list}")
    # print(f"\t-> CORRECT : {correct_index}")
    # print(f"\t-> WRONG   : {wrong_index}\n")
    print(f"\nVous avez trouvé {len(correct_index)} lettre(s).")
    print(f"Vous avez trouvé {len(wrong_index)} lettre(s) mal placée(s).")

if code == guess :
    print(f"\n\t-> Nice ! Tu as trouvé le code {code}.")
else :
    print(f"\n\t-> Dommage, le code était {code}.")





# from random import randint

# CODE_LENGHT = 4
# COUNT = 5
# LETTERS = ["a", "b", "c", "d", "e", "f"]
# code = []

# # Génération du code aléatoire
# for _ in range(CODE_LENGHT) :
#     index = randint(0, len(LETTERS) - 1)
#     letter = LETTERS[index]
#     code.append(letter)

# guess = ""

# for i in range(COUNT) :
#     if guess != code :
#         while len(guess) != len(code) :
#             guess = input(f"\nEntrez {CODE_LENGHT} lettres : ")
#             guess_list = list(guess)

#         correct_index = []
#         wrong_index = []
#         # Gestion des lettres bien placées
#         for i_guess in range(CODE_LENGHT) :
#             if guess_list[i_guess] == code[i_guess] :
#                 correct_index.append(i_guess)

#         # Gestion des lettres mal placées
#         for i_guess in range(CODE_LENGHT) :
#             for i_code in range(CODE_LENGHT) :
#                 if guess_list[i_guess] == code[i_code] :
#                     if i_code not in correct_index and i_guess not in correct_index and i_code not in wrong_index :
#                         wrong_index.append(i_code)
#                         break

#         # ! DEBUG
#         print(f"\t-> CODE    : {code}")
#         print(f"\t-> REPONSE : {guess_list}")
#         print(f"\t-> CORRECT : {correct_index}")
#         print(f"\t-> WRONG   : {wrong_index}\n")
#         print(f"Vous avez trouvé {len(correct_index)} lettre(s).")
#         print(f"Vous avez trouvé {len(wrong_index)} lettre(s) mal placée(s).")
#         guess = input(f"\n-> Entrez 4 lettres ({COUNT - i} essai(s)) : ")
#         guess_list = list(guess)

# if guess != code :
#     print(f"\n\t-> Dommage, le code était {code}.")