# VOWELS = ["a", "e", "i", "o", "u", "y"]
VOWELS = "aeiouy"

word = input("Mot: ")

count = 0

for letter in word:
    if letter in VOWELS:
        count = count + 1

print("Il y a " + str(count) + " voyelles dans '" + word + "'." )