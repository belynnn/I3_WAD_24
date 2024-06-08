#          0  1  2  3    0  1  2  3    0  1   2   3
# grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# #             0             1              2

# for line in range(3) :
#     text = ""
#     for column in range(4) :
#         value = grid[line][column] / 2
#         text = text + str(value) + " "
#     print(f"{text}")



####################################
# CORRECTION                       #
####################################
#        0  1  2  3    0  1  2  3    0  1   2   3
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#             0             1              2

# for line in range(len(grid)) :
#     text = ""
#     for column in range(len(grid[line])) :
#         text += f"{grid[line][column] / 2} "
#     print(text)

for line in grid :
    text = ""
    for value in line :
        text += f"{value / 2} "
    print(text)