# Ennoncé
"""
[v] Créez une liste vide.
[v] Demandez à l'utilisateur d'entrer un mot au clavier.
[v] Tant que le mot entré n'est pas "stop":
[v] Demandez à quel index le mot doit être placé dans la liste
[v] Ajoutez le mot à la liste, à l'index demandé
[v] Redemandez un nouveau mot à l'utilisateur
[v] Affichez la liste finale.
"""

word_list = []

user_word = input("Entrez un mot (stop pour finir) : ")

while user_word != "stop" :
    user_index = int(input("Entrez un index : "))

    word_list.insert(user_index, user_word)

    user_word = input("Entrez un mot (stop pour finir) : ")

print(word_list)



####################################
# CORRECTION                       #
####################################
# words = []

# word = input("Mot : ")

# while word != "stop" :
#     index = int(input("Index : "))

#     words.insert(index, word)
    
#     word = input("Mot : ")

# print(words)