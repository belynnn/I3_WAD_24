word = input("Entrez un mot (end pour finir) ")
counter = 1

while word != "end":
    if len(word) > 0 and word[0] == "t":
        print(word + "!!!")
    word = input("Entrez un mot (end pour finir) ")
    counter = counter + 1

print(counter)
