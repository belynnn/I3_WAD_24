from random import randint


CODE_LENGTH = 4
LETTERS = ["a", "b", "c", "d", "e", "f"]
ESSAIS_MAX = 12

code = []

for _ in range(CODE_LENGTH):
    index = randint(0, len(LETTERS) - 1)
    letter = LETTERS[index]
    code.append(letter)

guess = None

essai = 0

while guess != code and essai < ESSAIS_MAX :

    print(f"Essai(s) restant(s): {ESSAIS_MAX - essai}")
    essai += 1
    guess = input("Entrez une proposition de " + str(CODE_LENGTH) + " lettres: ")
    while len(guess) != CODE_LENGTH:
        guess = input("Entrez une proposition de " + str(CODE_LENGTH) + " lettres: ")

    guess = list(guess)

    correct = []
    for i in range(CODE_LENGTH):
        if code[i] == guess[i]:
            correct.append(i)
    print(str(len(correct)) + " lettres bien placées.")

    wrong = []

    # Vérification des lettres mal placées
    for i_guess in range(CODE_LENGTH):
        for i_code in range(CODE_LENGTH):
            if guess[i_guess] == code[i_code]:
                if i_code not in correct:
                    if i_guess not in correct:
                        if i_code not in wrong:
                            wrong.append(i_code)
                            break

    print(str(len(wrong)) + " lettres mal placées.")

if code == guess:
    print("Bravo!!")
else:
    print(f"Désolé, le code était: {code}")