from random import randint

def random_word(num_letters):
    letters = ["a", "h", "k", "o", "n", "s", "t"]
    
    word = ""
    
    for i in range(num_letters):
        index = randint(0, len(letters) - 1)
        letter = letters[index]
        word = word + letter

    return word

n = int(input("Combien de lettres: "))
result = random_word(n)
print(result)
