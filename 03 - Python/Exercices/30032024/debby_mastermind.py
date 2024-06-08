from random import randint

# ? Affectations relative à la génération + reste
letters = ["a", "b", "c", "d", "e", "f"]
code = []
len_code = len(code) # slide128 # à n'utiliser que pour la génération de code

# ? Génération aléatoire du code à découvrir
for letter in range(len_code) :
    letter = randint(0, len(letters)-1)
    code.append(letters[letter])
code = ["a", "b", "a", "d"] # code forcé pour debug
print(code[0])
print(f"\n\n  ->  CODE : {code}") # ! code généré

# ? Affectations relatives au while + reste
count = 5
answer = ""
wrong_index = []
correct_index = []

# ? Tant que différent de code et que longueur différent
while answer != code or len(answer) != len(code) :
    answer = input("Entrez 4 lettres : ")
    answer = list(answer)
    print(f"  -> ANSWER  : {answer}")

    # ? FOR : Si, au même index, la réponse est == au code : append index correct
    for i_answer in range(len(answer)) :
        # print(len(code)) - utilisé en debug
        for i_code in range(len(code)) :
            # print("code str") - utilisé en debug
            if answer[i_answer] == code[i_code] :
                correct_index.append(i_answer)
                if code[i_code] not in correct_index and answer[i_answer] not in correct_index and code[i_code] not in wrong_index :
                    wrong_index.append(i_code)
                    break

    print(f"  -> CORRECT : {correct_index}") # à changer par len(correct_index) à la fin
    print(f"  -> WRONG   : {wrong_index}") # à changer par len(wrong_index) à la fin

    if answer == code :
        print("Waa t'es trop fort!")