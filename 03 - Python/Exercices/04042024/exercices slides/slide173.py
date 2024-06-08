# grid = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

# Peut être écrit comme ceci :
grid = [["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"]]

# Peut également être écrit comme ceci :
line_1 = ["a", "b", "c"]
line_2 = ["d", "e", "f"]
line_3 = ["g", "h", "i"]

grid2 = [line_1, line_2, line_3]

# Visuellement ça donnerait =
"""
   __ ___ ___ __
0  | a | b | c |
1  | d | e | f |
2  | g | h | i |
   -------------
     0   1   2
"""

# Si on veut aficher la première ligne -> ["a", "b", "c"] :
print(grid[0])

# Si on souhaite afficher la lettre b de la line_0 -> "b"
print(grid[0][1])