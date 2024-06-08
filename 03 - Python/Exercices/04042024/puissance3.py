"""
Aligner 3 jetons par joueurs (2) horizontalement, verticalement ou en diagonale

Joueur 1
3 jetons X

Joueur 2
3 jetons O

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