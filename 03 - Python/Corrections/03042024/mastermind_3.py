from random import randint


CODE_LENGTH = 4
LETTERS = ["a", "b", "c", "d", "e", "f"]

code = []

for _ in range(CODE_LENGTH):
    index = randint(0, len(LETTERS) - 1)
    letter = LETTERS[index]
    code.append(letter)

print(code)
guess = None

while guess != code :

    guess = input("Entrez une proposition de " + str(CODE_LENGTH) + " lettres: ")
    while len(guess) != CODE_LENGTH:
        guess = input("Entrez une proposition de " + str(CODE_LENGTH) + " lettres: ")

    guess = list(guess)

    correct = []
    for i in range(CODE_LENGTH):
        if code[i] == guess[i]:
            correct.append(i)
    print(str(len(correct)) + " lettres bien placées.")

    # Vérification des lettres mal placées
    for i_guess in range(CODE_LENGTH):
        for i_code in range(CODE_LENGTH):
            if guess[i_guess] == code[i_code]

