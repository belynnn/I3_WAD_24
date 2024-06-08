from random import randint

letter_list = ["a", "b", "c", "d", "e", "f"]

code = []

for index in range(4) :
    letter = randint(0, len(letter_list)-1)
    code.append(letter_list[letter])
    code = ["b", "b", "d", "e"] # dbde

print(f"  ->  CODE : {code}")

# answer = ""
answer = ""
correct_index = []
wrong_index = []
notin_index = []
count = 5


for i in range(count) :
    if answer != code :
        while len(answer) != len(code) :
            answer = list(input("Entrez 4 lettres : "))

        for j in range(len(answer)) :
            if answer[j] == code[j] : # ! se base sur l'index, pas la lettre
                correct_index.append(j)

            for k in range(len(code)) :

                # if answer[i_answer] != code[i_code] and answer[i_answer] in code and code[i_answer] not in correct_index and answer[i_answer] not in correct_index and code[i_code] not in wrong_index :
                if answer[j] == code[k] and answer[j] in code and k not in correct_index and j not in correct_index and j not in wrong_index :
                    wrong_index.append(j)
                    break

        print(f"  ->  CORRECT    : {correct_index}") # devra être modifié en len(correct_index) pour afficher le total de bonne lettres trouvées
        print(f"  ->  WRONG      : {wrong_index}") # devra être modifié en len(wrong_index) pour afficher le total de lettres trouvées MAIS mal placées
        
        correct_index = []
        wrong_index = []

        answer = list(input(f"Entrez 4 lettres ({count - i} essai(s)) : "))

if answer == code :
    print("Walla t'es trop fort.")
else :
    print(f"Le code était {code}")