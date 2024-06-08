# tableau = [ # Index des colonnes -> 0    1    2    3    4
#   """Index de la ligne 1 -> 0 """ [".", ".", ".", ".", "."],
#   """Index de la ligne 2 -> 1 """ [".", ".", ".", ".", "."],
#   """Index de la ligne 3 -> 2 """ [".", ".", ".", ".", "."],
#   """Index de la ligne 4 -> 3 """ [".", ".", ".", ".", "."],
#   """Index de la ligne 5 -> 4 """ [".", ".", ".", ".", "."]]

# def display_grid(grid) :
#     for line in range(len(grid)) :
#         text = ""
        
#         for column in range(len(grid[line])) :
#             text += grid[line][column]
#         print(text)

#         text = ""
#         for last_line in range(len(grid[0])) :
#             text += f" {last_line}"
#         print(f" {text}")

# display_grid(tableau)



# Pour Jessica
tableau = [[".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."]]

def display_grid(grid, qtylist, listlenght) :
    for line in range(len(grid)) :
        text = ""
        
        for column in range(len(grid[line])) :
            text += grid[line][column]
        print(text)

        text = ""
        for last_line in range(len(grid[0])) :
            text += f" {last_line}"
        print(f" {text}")

user_qtylist = int(input("Nombre de lignes : "))
user_listlenght = int(input("Nombre de colonnes : "))

# générer le tableau
# initialisation d'une boucle for
# pour chaque ligne :
    # injecter le nombre de ligne (list) par rapport à 'user_qtylist'
    # pour chaque colonne :
        # injecter le nombre de colonne (value) par rapport à 'user_listlenght' dans leur ligne (list) respective

display_grid(tableau, user_qtylist, user_listlenght)