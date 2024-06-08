from random import randint

def random_word(number, list):
    if number > len(list):
        number = len(list)

    word = ""
    for _ in range(number):
        index = randint(0, len(list) -1)
        word += list.pop(index)
        
    return word

#   --- MAIN PROGRAM ---

LETTERS = ["a", "l", "o", "h", "b", "k", "j"]

user_number = int(input(f"Entrez un nombre entre 1 et {len(LETTERS)} : "))

print(random_word(user_number, LETTERS))



# def random_word(number, list) :
#     LETTERS = ["a", "i", "l", "n", "o", "r", "s", "t"]
    
#     word = ""
#     for _ in range(number) :
#         index = randint(1, len(LETTERS) -1)
        
#         LETTERS = LETTERS.remove(index)

#     return word

# #   --- MAIN ---

# user_number = int(input(f"Entrez un nombre entre 1 et 8 : "))

# print(random_word(user_number, ["a", "e", "i", "o", "u", "y", "k", "j"]))