#page 180

table = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

for line in range(len(table)):
    txt = ""
    for column in range(len(table[line])):
        txt += f"{table[line][column] / 2} "
    print(txt)