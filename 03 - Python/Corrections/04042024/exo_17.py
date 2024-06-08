VALUES = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
SYMBOLS = ["Club", "Diamond", "Heart", "Spade"]

for symbol in SYMBOLS:
    for value in VALUES:
        print(f"{value} of {symbol}")