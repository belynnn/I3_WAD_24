def count_letter(word, letter):

    count = 0

    for l in word:
        if l == letter:
            count += 1

    return count

# --- main program ---

word = input("Mot: ")
letter = input("Lettre: ")

print(f"Il y a {count_letter(word, letter)} fois '{letter}' dans '{word}'.")