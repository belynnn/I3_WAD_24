# EXERCICE 1
# liste = ['a', 'b', 'c', 'd', 'e', 'f']
# print(list)

# EXERCICE 2
# list = ['I', 'really', 'love', 'Python']
# print(list[2])

# EXERCICE 3
# users = ['Jo', 'Alex', 'Graham', 'Kathleen']
# count = len(users)
# print(count)

# EXERCICE 4
# from random import randint

# liste = ['a', 'b', 'c', 'd', 'e', 'f']

# index = randint(0, len(liste)-1)

# print(liste)
# print(liste[index])

# EXERCICE 5
# users = ['Jo', 'Alex', 'Graham', 'Kathleen']
# print(users[len(users)-1]))

# EXERCICE 6
# list = ['I', 'really', 'love', 'Python']
# print(list[1:3])

# EXERCICE 7
# list = ['I', 'really', 'love', 'Python']
# print(list[:3])

# EXERCICE 8
# list = ['I', 'really', 'love', 'Python']
# print(list[1:])

# EXERCICE 9
# l = ['a', 'b', 'c', 'd', 'e', 'f']

# user = int(input("Donnez un nombre entre 0 et la longueur de la liste: "))

# while user > len(l)-1 or user < 0:
#     user = int(input("Donnez un nombre entre 0 et la longueur de la liste: "))

# print(l)
# print(l[:user])
# print(l[user:])

# EXERCICE 10
l = []

user = str(input("Pour arrêter, écrviez STOP.\nDonnez un mot: "))
l.append(user)

while user != "STOP":
    user = str(input("Pour arrêter, écrviez STOP.\nDonnez un mot: "))

    l.append(user)

print("Voici vos mots: " + str(l))

# EXERCICE 11
