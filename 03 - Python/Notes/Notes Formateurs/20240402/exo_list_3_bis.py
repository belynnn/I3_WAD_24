words = []
word = None

while word != 'stop':
    word = input("Mot: ")
    words.append(word)

word = word[:-1]
print(words)