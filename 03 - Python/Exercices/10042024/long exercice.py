#   --- CONSTANTES DE TEST ---
from random import randint

# TABLE_9 = [[1,2,3,4,5,6,7,8,9],
#          [10,11,12,13,14,15,16,17,18],
#          [19,20,21,22,23,24,25,26,27],
#          [28,29,30,31,32,33,34,35,36],
#          [37,38,39,40,41,42,43,44,45],
#          [46,47,48,49,50,51,52,53,54],
#          [55,56,57,58,59,60,61,62,63],
#          [64,65,66,67,68,69,70,71,72],
#          [73,74,75,76,77,78,79,80,81]]
# TABLE_line10 = [[1,2,3,4,5,6,7,8,9],
#                 [10,11,12,13,14,15,16,17,18],
#                 [19,20,21,22,23,24,25,26,27],
#                 [28,29,30,31,32,33,34,35,36],
#                 [37,38,39,40,41,42,43,44,45],
#                 [46,47,48,49,50,51,52,53,54],
#                 [55,56,57,58,59,60,61,62,63],
#                 [64,65,66,67,68,69,70,71,72],
#                 [73,74,75,76,77,78,79,80,81],
#                 [73,74,75,76,77,78,79,80,81]]
# TABLE_column10 = [[1,2,3,4,5,6,7,8,9],
#                   [10,11,12,13,14,15,16,17,18],
#                   [19,20,21,22,23,24,25,26,27],
#                   [28,29,30,31,32,33,34,35,36],
#                   [37,38,39,40,41,42,43,44,45,46],
#                   [46,47,48,49,50,51,52,53,54],
#                   [55,56,57,58,59,60,61,62,63],
#                   [64,65,66,67,68,69,70,71,72],
#                   [73,74,75,76,77,78,79,80,81]]



#   --- FONCTIONS ---
def verify_len_line_column(grid):
    if len(grid) > 9:
        print("Tableau trop grand.")
        quit()
    
    for line in range(len(grid)):
        if len(grid[line]) > 9:
            print("Tableau trop grand.")
            quit()

def display_grid(grid):
    verify_len_line_column(grid)

    for line in range(len(grid)):
        text = ""
        for column in range(len(grid[line])):
            if grid[line][column] < 10:
                text += f"{grid[line][column]}  "
            else:
                text += f"{grid[line][column]} "
        print(f"{text}")

def generate_grid(max_line, max_column):
    n = max_line * max_column

    grid = []

    count = 1
    for i_line in range(max_line):
        line = []
        for i_column in range(max_column):
            line.append(count)
            count += 1
        grid.append(line)
    
    return display_grid(grid)

def generate_snake_grid(max_line, max_column):
    n = max_line * max_column

    grid = []

    count = 1
    for i_line in range(max_line):
        line = []
        for i_column in range(max_column):
            line.append(count)
            count += 1
        if(i_line+1) % 2 == 0:
            line.reverse()
        grid.append(line)
    
    return display_grid(grid)


#   --- MAIN PROGRAM ---

display_format = ""
while display_format != "n" and display_format != "N" and display_format != "s" and display_format != "S" and display_format != "e" and display_format != "E" :
    display_format = input("Entrez N, S : ")

if display_format == "n" or display_format == "N":
    nb_line_user = int(input("Nombre de ligne (entre 1 et 9) : "))
    nb_column_user = int(input("Nombre de colonne (entre 1 et 9) : "))
    generate_grid(nb_line_user, nb_column_user)
elif display_format == "s" or display_format == "S":
    nb_line_user = int(input("Nombre de ligne (entre 1 et 9) : "))
    nb_column_user = int(input("Nombre de colonne (entre 1 et 9) : "))
    generate_snake_grid(nb_line_user, nb_column_user)
elif display_format == "e" or display_format == "E":
    print("Eeerrrr nop.")





# # generate_grid(nb_line_user, nb_column_user)
# generate_snake_grid(nb_line_user, nb_column_user)



# display_grid(TABLE_9)