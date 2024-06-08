# VOWELS = ["a", "e", "i", "o", "u", "y"]
VOWELS = "aeiouy"

word = input("Mot: ")

count = 0

for letter in word:
    if letter in VOWELS:
        count += 1

print(f"Il y a {count} voyelles dans '{word}'." )