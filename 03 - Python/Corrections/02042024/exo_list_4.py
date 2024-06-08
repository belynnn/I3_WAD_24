# page 120

words = []

word = input("Mot: ")

while word != "stop":
    index =input("Index: ")
    index = int(index)

    words.insert(index, word)
    
    word = input("Mot: ")

print(words)
