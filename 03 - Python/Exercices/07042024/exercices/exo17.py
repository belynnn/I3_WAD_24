"""
#! énoncé
A l'aide de 2 boucles, créez un script qui énumère toutes les cartes d'un jeu de cartes à jouer. Une des boucles concerne les symboles (cœur, carreau, pique, trèfle) et une autre les valeurs (as, deux, trois, …, dame, roi).

#! décripteur Belynn1312

"""

card_symbol = ["♥️", "♦️", "♠️", "♣️"]
card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

for i in card_symbol :
    print(f"\n")
    for j in card_value :
        print(f"{j} {i}")