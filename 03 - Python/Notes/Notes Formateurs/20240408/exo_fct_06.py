def remove_letter(word):

    vowels = "aeiouy"
    new_word = ""

    for letter in word:
        if letter not in vowels:
            new_word += letter

    return new_word

# --- main --- 

word = input("Mot: ")
print(remove_letter(word))