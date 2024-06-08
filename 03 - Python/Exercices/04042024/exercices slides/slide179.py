#         0    1    2      0    1    2      0    1    2
grid = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
#              1                2                3
# Pour chaque ligne de mes lignes (tableau de 3 lignes)
for line in range(3) :
    text = ""
    # Pour chaque colonne de mes colonnes (tableau de 3 colonnes)
    for column in range(3) :
        text += grid[line][column]
    print(f"{text}\n")