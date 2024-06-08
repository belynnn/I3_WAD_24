from random import randint

# def random_word(number):
#     LETTERS = ["a", "i", "l", "n", "o", "r", "s", "t"]

#     if number > len(LETTERS):
#         number = 8
#         # print("Nombre de lettres trop grand.")
#         # return None

#     word = ""
#     for _ in range(number):
#         index = randint(0, len(LETTERS) -1)
#         word += LETTERS.pop(index)
        
#     return word

# LETTERS = ["a", "i", "l", "n", "o", "r", "s", "t"]

# user_number = 0

# while user_number < 1 or user_number > len(LETTERS):
#     user_number = int(input(f"Entrez un nombre entre 1 et {len(LETTERS)} : "))

# print(random_word(user_number))



# # # # # # # # # # # # # # # # # # # # # # # # # # #
# ---> CORRECTION
# # # # # # # # # # # # # # # # # # # # # # # # # # #
def random_word(number):
    LETTERS = ["a", "i", "l", "n", "o", "r", "s", "t"]
    
    if number > len(LETTERS):
        number = len(LETTERS)

    word = ""
    for _ in range(5):
        index = randint(0, len(LETTERS) -1)
        word += LETTERS.pop(index)
        
    return word

#   --- MAIN PROGRAM ---

user_number = int(input("Combien de lettres ? : "))

result = random_word(user_number)
print(result)



# ///////////////////////////////////////////////////
# ---> OLD
# ///////////////////////////////////////////////////
# def random_word(number) :
#     LETTERS = "ailnorst"
    
#     word = ""
#     for _ in range(number) :
#         letter = LETTERS[randint(0, len(LETTERS) - 1)]
        
#         LETTERS = LETTERS.replace(letter, "")
#         word = word.replace(letter, letter)

#         word += letter

#     return word

# #   --- MAIN ---
# LETTERS = "ailnorst"

# user_number = 0

# while user_number < 1 or user_number > len(LETTERS):
#     user_number = int(input(f"Entrez un nombre entre 1 et {len(LETTERS)} : "))

# print(random_word(user_number))