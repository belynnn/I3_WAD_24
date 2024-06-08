def multiply_table(number) :
    multiply_number = number
    total_decimal_number = 10

    for i in range(total_decimal_number) :
        print(f"{i+1} x {multiply_number} = {(i+1)*multiply_number}")

user_number = int(input("Entrez un nombre : "))

multiply_table(user_number)