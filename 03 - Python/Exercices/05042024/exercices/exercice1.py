# # FONCTION
# # doit renvoyer le mot inverse
# def reversed_word(word) :
#     result = word[-1:-(len(word)+1):-1]

#     return result

# # PROGRAMME PRINCIPAL
# # recevoir un mot et renvoyé le mot
# user_word = input("Entrez un mot : ")
# final_result = reversed_word(user_word)

# print(f"Votre mot '{user_word}' inversé donne '{final_result}'.")

# # String slicing
# String = 'ASTRING'
# s1 = slice(3)
# s2 = slice(1, 5, 2)
# s3 = slice(-1, -12, -1)
 
# print("String slicing")
# print(String[s1])
# print(String[s2])
# print(String[s3])



####################################
# CORRECTION                       #
####################################
# V1
# def invert_word(word) :
#     result = ""
#     for i in range(-1, -len(word) -1, -1) :
#         result += word[i] 

#     return result

# user_word = input("Entrez un mot : ")
# print(invert_word(user_word))

# V2
# def invert_word(word) :
#     result = ""
#     i = -1
#     for letter in word :
#         pick = word[i]
#         result = result + pick 
#         i -= 1

#     return result

# user_word = input("Entrez un mot : ")
# print(invert_word(user_word))

# V3
def invert_word(word) :
    result = ""
    for letter in word :
        result = letter + result

    return result

user_word = input("Entrez un mot : ")
print(invert_word(user_word))

# exemple
# bonjour
# b + "" -> "b"
# o + "b" -> "ob"
# n + "ob" -> "nob"