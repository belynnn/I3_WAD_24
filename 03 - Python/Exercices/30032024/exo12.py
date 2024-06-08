""" # ! Énnoncé 
Créez un programme qui va demander à l'utilisateur d'entrer des nombres.
Le programme continuera à en demander tant que l'utilisateur n'aura pas donné deux nombres identiques d'affilée.
En fin de programme, affichez la somme de tous les nombres entrés par l'utilisateur.
"""

number_list = []
sum = 0

while len(number_list) < 2 or number_list[-2] != number_list[-1]:
    number = int(input("Entrez un nombre : "))
    number_list.append(number)

for i in number_list :
    sum += i

print(f"Somme totale : {sum}")



# ! OLD bug + répétition, comment y remédier ?
# nombres = []
# sum = 0

# while len(nombres) < 2 :
#     nombre = int(input("Entrez un nombre : "))
#     nombres.append(nombre)

# while nombres[-2] != nombres[-1] :
#     nombre = int(input("Entrez un nombre : "))
#     nombres.append(nombre)

# for i in number_list :
#     sum += i
# print("La somme des nombres est", somme)



# # ! OLD prise de tête
# # number_list = []

# # number = int(input("Entrez un nombre : "))
# # number_list.append(number)
# # next_number = int
# # sum = number

# # for i in range(number_list[0],number_list[-1]) :
# #     if number_list[-2] != number_list[-1] : 
# #         next_number = int(input("Entrez un nombre : "))

# #         number_list.append(next_number)

# #         sum += next_number

# # print("toto")



# # # ! OLD début
# # # number = int(input("Entrez un nombre : "))

# # # sum = number

# # # print(f"-> Somme totale : {sum}")