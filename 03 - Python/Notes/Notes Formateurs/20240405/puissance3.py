

def display_grid(grid):
    for line in range(len(grid)):
        text = ""
        for col in range(len(grid[line])):
            text = text + " " + grid[line][col]
        print(str(line) + text)

    text = ""
    for last_line in range(len(grid[0])):
        text = text + f" {last_line}"
    print(f" {text}")

def display_grid2(grid):
    i = 0
    for line in grid:
        text = ""
        for element in line:
            text = text + " " + element
        print(str(i) + text)
        i = i + 1

    text = ""
    i = 0
    for last_line in grid[0]:
        text = text + f" {i}"
        i = i + 1
    print(f" {text}")

def check_winner(grid, current_player):
    return current_player == 2



tableau = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
]

winner = None
player = 1

while winner == None:
    display_grid(tableau)

    # On joue un tour
    if check_winner(tableau, player):
        winner = player
    else:
        if player == 1:
            player = 2
        else:
            player = 1
