from random import randint


TOKEN_1 = "💚"
TOKEN_2 = "💜"

def get_token(player):
    if player == 1:
        return TOKEN_1
    return TOKEN_2

# Afficher game board vide
def display_grid(grid):
    for line in range(len(grid)):
        text = ""
        for col in range(len(grid[line])):
            text = text + " " + grid[line][col]
        print(str(line) + text)

    text = ""
    for last_line in range(len(grid[0])):
        text = text + f"  {last_line}"
    print(f" {text}")

    # Afficher game board
    # # def display_grid2(grid):
    #     i = 0
    #     for line in grid:
    #         text = ""
    #         for element in line:
    #             text = text + " " + element
    #         print(str(i) + text)
    #         i = i + 1

    #     text = ""
    #     i = 0
    #     for last_line in grid[0]:
    #         text = text + f"  {i}"
    #         i = i + 1
    #     print(f" {text}")

def check_vertical(grid, column, line):
    # si la ligne est plus grande ou égale à 3, alors return false
    if line >= 3:
        return False
    # si les deux jetons en dessous sont égaux au jeton (line +1 et +2, column), alors on renvoit True sinon ou renvoit False
    if grid[line][column] == grid[line + 1][column]:
        if grid[line][column] == grid[line + 2][column]:
            return True

    return False

def check_horizontal(grid, column, line):
    # Vérifier que les jetons ne débordent pas de colonnes
        # si la colonne <=2
        # si la colonne >=2
        # si la colonne >=1 et colonne <=3
    # Le jeton joué est entouré de jetons identique (avant et après)
    if column >= 1 and column <= 3:
        if grid[line][column] == grid[line][column + 1] and grid[line][column] == grid[line][column - 1]:
            return True

    # Les jetons à droite sont identique à celui joué (après)
    if column <= 2:
        if grid[line][column] == grid[line][column + 1] and grid[line][column] == grid[line][column + 2]:
            return True
        
    # Les jetons à gauche sont identique à celui joué (avant)
    if column >= 2:
        if grid[line][column] == grid[line][column - 1] and grid[line][column] == grid[line][column - 2]:
            return True
    
    return False

def check_diagonal(grid, column, line):
    # # # # # # # # # # # # # # 
    # Diagnole vers la gauche
    if line <= 2 and column <= 2:
        # ligne + 1, colonne + 1
        if grid[line][column] == grid[line + 1][column + 1] and grid[line][column] == grid[line + 2][column + 2]:
            return True
        
    if line >= 2 and column >= 2:
        # ligne - 1, colonne - 1
        if grid[line][column] == grid[line - 1][column - 1] and grid[line][column] == grid[line - 2][column - 2]:
            return True
        
    if column >= 1 and line >= 1 and column <= 3 and line <= 3:
        if grid[line][column] == grid[line + 1][column + 1] and grid[line][column] == grid[line - 1][column - 1]:
            return True

    # # # # # # # # # # # # # # 
    # Diagnole vers la droite
    if line >= 2 and column <= 2:
        # ligne - 1, colonne + 1
        if grid[line][column] == grid[line - 1][column + 1] and grid[line][column] == grid[line - 2][column + 2]:
            return True
        
    if line <= 2 and column >= 2:
        # ligne + 1, colonne - 1
        if grid[line][column] == grid[line + 1][column - 1] and grid[line][column] == grid[line + 2][column - 2]:
            return True

    if line >= 1 and line <= 3 and column >= 1 and column <= 3:
        if grid[line][column] == grid[line + 1][column - 1] and grid[line][column] == grid[line - 1][column + 1]:
            return True
    return False

def check_winner(grid, column, current_player):
    line = 0
    while grid[line][column] == "⬜" :
        line += 1

    if check_vertical(grid, column, line):
        return True
    
    if check_horizontal(grid, column, line):
        return True
    
    if check_diagonal(grid, column, line):
        return True

    return False

def check_stale(grid):
    for value in grid[0]:
        if value == "⬜":
            return False
    return True

def play(grid, column, player):
    # trouver pour la colonne passée en paramètre la 1ere ligne vide
    line = 4

    while grid[line][column] != "⬜" and line > -1:
        line -= 1
    # placer le bon token dans la colonne à la ligne trouvée
    grid[line][column] = get_token(player)
    # si colonne remplie, tour passé, passe au suivant
    return grid

#   --- MAIN PROGRAM ---

tableau = [
    ["⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜"]]

winner = None
player = 1

while winner == None:
    display_grid(tableau)

    # On joue un tour
    # Demande à l'user quelle colonne
    # column = int(input(f"Joueur {get_token(player)}, quelle colonne ? : "))
    column = randint(0,3)
    play(tableau, column, player)

    if check_winner(tableau, column, player):
        winner = player
    else:
        if check_stale(tableau):
            tableau = [
                ["⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜"]]
        if player == 1:
            player = 2
        else:
            player = 1

display_grid(tableau)
print(f" -> Nicelelelelele, player {get_token(winner)} !")