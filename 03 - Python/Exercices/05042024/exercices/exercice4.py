# from random import randint

# def random_lenght_list(number) :
#     number_list = []
    
#     for _ in range(number) :
#         random_number = randint(1, 6)
#         number_list.append(random_number)

#     return number_list

# n = int(input("Entrez un nombre : "))
# result = random_lenght_list(n)

# print(result)

# CORRECTION
from random import randint

def rnd_numbers(n) :
    numbers = []

    for _ in range(n) :
        numbers.append(randint(1,6))
    
    return numbers

table = rnd_numbers()
print(table)