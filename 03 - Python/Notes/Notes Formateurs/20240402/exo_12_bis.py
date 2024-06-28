# /!\ Moins performant parce que list !!! /!\ 

numbers = []

number = input("Nombre: ")
number = int(number)
numbers.append(number)

number = input("Nombre: ")
number = int(number)
numbers.append(number)

while numbers[-2] != numbers[-1]:
    number = input("Nombre: ")
    number = int(number)
    numbers.append(number)

print("Somme: " + str(sum(numbers)))