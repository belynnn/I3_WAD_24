from random import randint

solution = randint(1, 10)

guess = None

tries = 0

while guess != solution and tries < 3:

    guess = int(input("Donnez un nombre entre 1 et 10: "))
    tries = tries + 1
    
    if guess < solution:
        print("Trop petit!")
    elif guess > solution:
        print("Trop grand...")
    else:
        print("C'est ça!")

if guess != solution:
    print("La bonne solution était " + str(solution))
