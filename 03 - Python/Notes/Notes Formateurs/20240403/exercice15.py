number = input("Entrez un nombre entier entre 1 et 100: ")
number = int(number)

while number < 1 or number > 100:
    number = input("Entrez un nombre entier entre 1 et 100: ")
    number = int(number)

# V1
# somme = 0
# i = 1
# while i <= number :
#     somme = somme + i
#     i = i + 1

# V2
# somme = 0
# while number > 0:
#     somme = somme + number
#     number = number - 1

# V3
somme = 0
for i in range(1, number+1):
    somme = somme + i

print(somme)


