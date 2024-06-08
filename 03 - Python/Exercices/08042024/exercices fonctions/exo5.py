# def count_specific_letter(word, letter) :
#     for letter in word :
#         if letter in word :
#             return sum(word[letter])
#         return False

# user_word = input("Entrez un mot : ")
# user_letter = input("Entrez une letter contenue dans le mot : ")

# result = count_specific_letter(user_word, user_letter)
# print(f"{result}")

# CORRECTION
def count_letter(word, letter) :
    count = 0

    for i in word :
        if i == letter :
            count += 1
    
    return count

word = input("Mot : ")
letter = input("Letter : ")
count = count_letter(word, letter)

print(f"Il y a {count} fois '{letter}' dans '{word}'.")