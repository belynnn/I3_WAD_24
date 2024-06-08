texte = "Comment ça va!"

if "?" in texte:
    print("C'était une question...")
elif "!" in texte:
    print("C'était une exclamation !")

# Example 2

from random import randint

results = []
for i in range(10):
    results.append(randint(1, 6))

print(results)
if 6 not in results:
    print("Aucun 6")
