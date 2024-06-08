# Ennoncé
"""
[v] Créez une liste vide.
[v] Demandez à l'utilisateur d'entrer un mot au clavier.
[v] Tant que le mot entré n'est pas "stop", ajoutez-le à la liste, et redemandez un nouveau mot à l'utilisateur.
[v] Affichez tous les mots entrés par l'utilisateur.
"""

response_list = []

user_response = input("Entrez un mot (stop pour finir) : ")

while user_response != "stop" :
    response_list.append(user_response)

    user_response = input("Entrez un mot (stop pour finir) : ")

print(response_list)



####################################
# CORRECTION                       #
####################################
words = []
word = input("Entrez un mot (stop pour finir) : ")

while word != "stop" :
    words.append(word)
    word = input("Entrez un mot (stop pour finir) : ")

print(words)