
def invert_word(word):

    result = ""
    for i in range(-1, -(len(word) + 1), -1):
        result = result + word[i]
    
    return result

def invert_word_v2(word):

    result = ""
    i = -1
    for letter in word:
        pick = word[i]
        result = result + pick
        i = i - 1
    
    return result

def invert_word_v3(word):
    result = word[-1:-(len(word)+1):-1]  # word[::-1]
    return result


def invert_word_v4(word):

    result = ""
    for letter in word:
        result = letter + result
    
    return result


user_word = input("Entrez un mot: ")
print(invert_word_v4(user_word))



