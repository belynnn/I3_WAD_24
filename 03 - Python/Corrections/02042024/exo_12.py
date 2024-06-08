previous = None

number = input("Nombre: ")
number = int(number)
sum_number = number

while number != previous:
    previous = number
    number = input("Nombre: ")
    number = int(number)
    sum_number = sum_number + number

print("Somme: " + str(sum_number))