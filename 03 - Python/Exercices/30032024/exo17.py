""" # ! Énnoncé 
A l'aide de 2 boucles, créez un script qui énumère toutes les cartes d'un jeu de cartes à jouer. Une des boucles concerne les symboles (cœur, carreau, pique, trèfle) et une autre les valeurs (as, deux, trois, …, dame, roi).
"""

card_symbol = ["♥️", "♦️", "♠️", "♣️"]
card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

# ! NEON
for symbol in card_symbol :
    print(symbol * 5)
    for value in card_value :
        print(symbol + " " + value + " " + symbol)
    print(symbol * 5)
    print()

# ! LINES
for symbol in card_symbol :
    for value in card_value :
        print(f"{value + symbol}", end=" ")
    print()
print()

# ! COLUMN
for value in card_value:
    for symbol in card_symbol:
        print(f"{value}{symbol}\t", end=" ")
    print()