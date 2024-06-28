VALUES = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
SYMBOLS = ["Club", "Diamond", "Heart", "Spade"]

for index_symbol in range(len(SYMBOLS)):
    for index_value in range(len(VALUES)):
        print(f"{VALUES[index_value]} of {SYMBOLS[index_symbol]}")