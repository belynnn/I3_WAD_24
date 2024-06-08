# # Exercices Python
# #?#########################
# #?
# #?   Exercice 1
# #?
# #?#########################

name = input("Quel est votre nom ? :")

print(name)



# #?#########################
# #?
# #?   Exercice 2
# #?
# #?#########################

name = input("Quel est votre nom ? :")

print("Saisie clavier: " + name)



# #?#########################
# #?
# #?   Exercice 3
# #?
# #?#########################

number = int(input("Entrez un nombre entre 0 et 10 : "))

print("Nombre : " + str(number))



# #?#########################
# #?
# #?   Exercice 4
# #?
# #?#########################

number = int(input("Entrez un nombre entre 0 et 10 : "))

if number > 10 :
    print("Ce nombre est plus grand que 10.")



# #?#########################
# #?
# #?   Exercice 5
# #?
# #?#########################

number = int(input("Entrez un nombre entre 0 et 10 : "))

if number > 10 :
    print("Ce nombre est plus grand que 10.")
else :
    print("Le nombre est plus petit ou égal à 10.")



# #?#########################
# #?
# #?   Exercice 6
# #?
# #?#########################

number = int(input("Entrez un nombre entre 0 et 10 : "))

if number >= 10 :
    print("Bravo!")
elif number > 8 :
    print("Pas mal.")
elif number > 5 :
    print("Mouais, bof")
else :
    print("Pas terrible")



# #?#########################
# #?
# #?   Exercice 7
# #?
# #?#########################

number = int(input("Entrez un nombre entre 1 et 10 : "))

while number < 1 or number > 10 :
    number = int(input("Entrez un nombre entre 1 et 10 : "))



# #?#########################
# #?
# #?   Exercice 8
# #?
# #?#########################
# #! Version chaton
password = None
correct_password = "Pyth0n"

attempt = 0
max_attempt = 3

while attempt < max_attempt and password != correct_password :
    password = input("Entrez le bon mot de passe : ")

    if password == correct_password or attempt == max_attempt :
        print("Mot de passe valide.")
    else :
        attempt += 1

if password != correct_password :
    print("Mot de passe incorrect.")

# #! Version formateur
PASSWORD = "Pyth0n"
user_password = input("Mot de passe : ")
tentatives = 1

while user_password != PASSWORD and tentatives < 3 :
    user_password = input("Mot de passe : ")
    tentatives += 1

if user_password == PASSWORD :
    print("Mot de passe correct.")
else :
    print("Mot de passe incorrect.")



# #?#########################
# #?
# #?   Exercice 9
# #?
# #?#########################

from random import randint

number1 = randint(1,6)
number2 = randint(1,6)
number3 = randint(1,6)

while number1 != number2 or number2 != number3 or number3 != number1 :
    number1 = randint(1,6)
    number2 = randint(1,6)
    number3 = randint(1,6)

    print(number1, number2, number3)



# #?#########################
# #?
# #?   Exercice 10
# #?
# #?#########################
# #! Version Chaton
user_number = int(input("Entrez le bon nombre (0) : "))
correct_number = 0
little = big = user_number

while user_number != correct_number :
    if user_number < little :
        little = user_number
    elif user_number > big :
        big = user_number

    user_number = int(input("Entrez le bon nombre (0) : "))

print(f"Le plus petit nombre est {little}")
print(f"Le plus grand nombre est {big}")

# #! Version formateur
number = int(input("Nombre : "))

greater = number
lower = number

while number != 0 :
    number = int(input("Nombre : "))

    if number < lower :
        lower = number
    elif number > greater :
        greater = number

print(f"Petit : {lower}")
print(f"Grand : {greater}")



# #?#########################
# #?
# #?   Exercice 11
# #?
# #?#########################
# #! Version Chaton
from random import randint

count = 0
number1 = randint(0,100)
number2 = randint(0,100)
print(f"Les deux nombres générés aléatoirement sont :\n{number1}\n{number2}\n")

sum = number1 + number2

result = int(input(f"Entrez la somme de {number1} et {number2} : "))

while result != sum :
    result = int(input(f"Erreur. Entrez la somme de {number1} et {number2} : "))

    count += 1

if result == sum :
    print(f"Vous avez entré {count} réponses éronnées.")

# #! Version formateur
from random import randint

n1 = randint(1, 99)
n2 = randint(1, 99)

errors = 0
answer = int(input(f"Entrez la somme de {n1} et {n2} : "))

while answer != (n1 + n2) :
    errors += 1
    answer = int(input(f"Entrez la somme de {n1} et {n2} : "))

print(f"Vous avez entré {count} réponses éronnées.")

# #! Version formateur AUTRE
from random import randint

n1 =  randint(0, 100)
n2 =  randint(0, 100)

errors = 0
answer = input(str(n1) + "+" +  str(n2) + "= ")
answer = int(answer)

while answer != (n1 + n2):
    errors = errors + 1
    answer = input(str(n1) + "+" +  str(n2) + "= ")
    answer = int(answer)

print("Tu as fait " + str(errors) + " erreur(s).")



# #?#########################
# #?
# #?   Exercice 12
# #?
# #?#########################
# #! Version Chaton
previous_number = int(input("Entrez des nombres : "))
sum = previous_number

continuer = True

while continuer :
    next_number = int(input("Entrez des nombres : "))
    sum += next_number

    if next_number == previous_number :
        continuer = False
    else :
        previous_number = next_number

print(f"La somme des nombres entrés est : {sum}")

# #! Version formateur SANS LISTE
previous = int(input("Nombre : "))
# OU
# previous = None
number = int(input("Nombre : "))
sum_number = number + previous

while number != previous :
    previous = number
    number = int(input("Nombre : "))

    sum_number += number

print(f"Somme totale : {sum_number}")

# #! Version formateur AVEC LISTE
numbers = []

number = int(input("Nombre : "))
numbers.append(number)

number = int(input("Nombre : "))
numbers.append(number)

while numbers[-2] != numbers[-1] :
    number = int(input("Nombre : "))
    numbers.append(number)

print(f"Somme totale : {sum(numbers)}")

# #! Version formateur AUTRE
previous = None

number = input("Nombre: ")
number = int(number)
sum_number = number

while number != previous:
    previous = number
    number = input("Nombre: ")
    number = int(number)
    sum_number = sum_number + number

print("Somme: " + str(sum_number))



# #?#########################
# #?
# #?   Exercice 13
# #?
# #?#########################
number = 10

while 0 < number :
    print(number)
    number -= 1 

if number == 0 :
    print("Décollage !")



# #?#########################
# #?
# #?   Exercice 14
# #?
# #?#########################
# #! Version Chaton
text = None
correct_text = "end"
value_to_search = "t"
count = 0

while text != correct_text :
    text = input("Entrez un mot (pour terminer, entrez end) : ")

    if text[0] == value_to_search :
        print(f"{text}!!!")

    if text == correct_text :
        print(f"-> Vous avez entré {count} mots.")

    count += 1

# #! Version formateur
word = input("Entrez un mot (end pour finir) : ")
counter = 1

while word != "end" :
    word = input("Entrez un mot (end pour finir) : ")
    
    if len(word) > 0 and word[0] == "t"  :
        print(f"{word}!!!")

    counter += 1
print(f"-> Vous avez entré {counter} mots.")



# #?#########################
# #?
# #?   Exercice 15
# #?
# #?#########################
# #! Version Chaton
number = int(input("Entrez un nombre entre 1 et 100 : "))
sum = 0

while number < 1 or number > 100 :
    number = int(input("Entrez un nombre entre 1 et 100 : "))

if number >= 1 or number <= 100 :
    for i in range(number+1) :
        sum += i

print(f"  ->  {sum}")

# #! Versions formateur
number = int(input("entrez un nombre : "))

while number < 1 or number > 100 :
    number = int(input("entrez un nombre : "))

# #! V 1.0
somme = 0
index = 1

while index <= number :
    somme += index
    index += index

# #! V 2.0
somme = 0

while number > 0 :
    somme += number
    number -= 1

# #! V 3.0
somme = 0
value = range(number+1)
somme = sum(value)

print(somme)



# #?#########################
# #?
# #?   Exercice 16
# #?
# #?#########################
# #! Version Chaton
vowel = ["a", "e", "i", "o", "u", "y"]
count = 0

text = input("Entrez un mot : ")

for i in text :
    if i in vowel :
        count += 1

print(f"  -> Il y a '{count}' voyelle(s) dans le mot '{text}'")

# #! Version formateur
# VOWELS = "aeiouy"

# word = input("Mot : ")

# count = 0

# for letter in word :
#     if letter in VOWELS :
#         count += 1

# print(f"Il y a '{count}' voyelles dans '{word}'.")



#?#########################
#?
#?   Exercice 17
#?
#?#########################
# #! Version Chaton
# card_symbol = ["♥️", "♦️", "♠️", "♣️"]
# card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

# # ! NEON
# for symbol in card_symbol :
#     print(symbol * 5)
#     for value in card_value :
#         print(symbol + " " + value + " " + symbol)
#     print(symbol * 5)
#     print()

# # ! LINES
# for symbol in card_symbol :
#     for value in card_value :
#         print(f"{value + symbol}", end=" ")
#     print()
# print()

# # ! COLUMN
# for value in card_value:
#     for symbol in card_symbol:
#         print(f"{value}{symbol}\t", end=" ")
#     print()

# #! Version formateur
# SYMBOLS = ["♥️", "♦️", "♠️", "♣️"]
# VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

# for value in VALUES :
#     for symbol in SYMBOLS :
#         print(f"{value} of {symbol}")



#?#########################
#?
#?   MASTERMIND
#?
#?#########################
# #! Version formateur
# from random import randint

# CODE_LENGTH = 4
# LETTERS = ["a", "b", "c", "d", "e", "f"]
# ESSAIS_MAX = 12

# code = []

# for _ in range(CODE_LENGTH):
#     index = randint(0, len(LETTERS) - 1)
#     letter = LETTERS[index]
#     code.append(letter)

# guess = None

# essai = 0

# while guess != code and essai < ESSAIS_MAX :

#     print(f"Essai(s) restant(s): {ESSAIS_MAX - essai}")
#     essai += 1
#     guess = input("Entrez une proposition de " + str(CODE_LENGTH) + " lettres: ")
#     while len(guess) != CODE_LENGTH:
#         guess = input("Entrez une proposition de " + str(CODE_LENGTH) + " lettres: ")

#     guess = list(guess)

#     correct = []
#     for i in range(CODE_LENGTH):
#         if code[i] == guess[i]:
#             correct.append(i)
#     print(str(len(correct)) + " lettres bien placées.")

#     wrong = []

#     for i_guess in range(CODE_LENGTH):
#         for i_code in range(CODE_LENGTH):
#             if guess[i_guess] == code[i_code]:
#                 if i_code not in correct:
#                     if i_guess not in correct:
#                         if i_code not in wrong:
#                             wrong.append(i_code)
#                             break

#     print(str(len(wrong)) + " lettres mal placées.")

# if code == guess:
#     print("Bravo!!")
# else:
#     print(f"Désolé, le code était: {code}")