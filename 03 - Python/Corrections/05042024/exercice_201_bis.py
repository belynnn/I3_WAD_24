from random import randint

def rand_letter():
    letters = ["a", "h", "k", "o", "n", "s", "t"]
    index_in_letters = randint(0, len(letters)-1)
    letter = letters[index_in_letters]
    return letter

def random_word(num_letters):

    word = ""
    for i in range(num_letters):
        word = word + rand_letter()
    
    return word


n = int(input("Combien de lettres: "))
result = random_word(n)
print(result)
