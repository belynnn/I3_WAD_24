"""
Aligner 3 jetons par joueurs (2) horizontalement, verticalement ou en diagonale

Vide :
.

Joueur 1 :
♥

Joueur 2 :
♣

Grille de 5x5
   __ ___ ___ ___ ___ __
0  | . | . | . | . | . |
1  | . | . | . | . | . |
2  | . | . | . | . | . |
3  | . | . | . | . | . |
4  | . | . | . | . | . |
   ---------------------
     0   1   2   3   4
     
Le joueur selectionne une colonne pour mettre son jeton
    -> Le jeton va tomber jusqu'à la case la plus basse de cette colonne
Vérification si alignement de 3
    -> SI alignement de 3, le joueur gagne
    -> SINON, tour du joueur suivant
Si après un coup non gagne le tableau est rempli, il se vide et demande au joueur suivant de rejouer


"""
# Initialisation
# EXPLICATIONS FORMATEUR :
#     - fonction reçoit 1 tableau paramètre
#         --> afficher contenu tableau ligne par ligne
#     - afficher les numéro des lignes et colonnes
#         --> /!\ ne doit pas être dans le tableau (doit être affiché dans la fonction)
# variable winner = None
# Tant que le winner est == à None, continuer de jouer
# 
# Tour de jeu, mettre une pièce et vérifier si quelqu'un à gagner. 
    #   Si un joueur gagne, le jeu s'arrête, 
    #   sinon, on passe au joueur suivant.
# fonction paramètre, tableau, joueur
    #   ma_fonction(tableau, joueur)
# 
# Choisir la colonne à laquelle on veut jouer
# faire descendre les jetons ne vérifiant ce qu'il y a dans la colonne

# FONCTION(S)
def print_board(grid) :
    for line in range(len(grid)) :
        text = ""
        for column in range(len(grid[line])) :
            text += f"{grid[line][column]} "

        print(f"{line} {text}")
    
    text = ""
    for last_line in range(len(grid[0])) :
        text += f" {last_line}"
    print(f" {text}")

def check_winner(grid, current_player) :
    return current_player == 2
    # if current_player == 2 :
    #     return True
    # elif current_player == 1 :
    #     return False
    # else:
    #     return False
    # return False


# INITIALISATION
board_game = [[".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."]]

winner = None
player = 1


# PROGRAMME
while winner == None :
    print_board(board_game)

    # On joue un tour
    # On vérifie si gagnant
    if check_winner(board_game, player) :
        winner = player
    else :
        if player == 1 :
            player = 2
        else :
            player = 1


# Déclaration de la victoire