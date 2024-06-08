def remove_letter(word):

    vowels = "aeiouy"
    new_word = word

    for letter in word:
        if letter in vowels:
            new_word = new_word.replace(letter, "")

    return new_word

# --- main --- 

word = input("Mot: ")
print(remove_letter(word))