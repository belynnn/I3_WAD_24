#page 180

table = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

for line in table:
    txt = ""
    for value in line:
        txt += f"{value / 2} "
    print(txt)

    