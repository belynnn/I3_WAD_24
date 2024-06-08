def delete_vowels(word) :
    for letter in word :
        if letter in "aeiouy" :
            word = word.replace(letter, "♥")

    return word

print(delete_vowels("telegramme"))

# CORRECTION

def remove_letter(word) :
    VOWELS = "aeiouy"
    new_word = ""

    for letter in word : 
        if letter not in VOWELS :
            new_word += letter
    
    return new_word

word = input("Word : ")
print(remove_letter(word))