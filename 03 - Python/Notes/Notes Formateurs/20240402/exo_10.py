number = input("Nombre: ")
number = int(number)

greater = number
lower = number

while number != 0:
    number = input("Nombre: ")
    number = int(number)
    
    if number < lower:
        lower = number
    elif number > greater:
        greater = number

print("Plus grand: " + str(greater))
print("Plus petit: " + str(lower))