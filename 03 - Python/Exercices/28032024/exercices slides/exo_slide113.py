from random import randint

number_list = [42, 73, 19, 25, 13, 86]

user_number = int(input("1) Entrez un nombre entre 0 et 5 : "))
user_lenght_list = user_number - 1

while user_number < 0 or user_number >= len(number_list) :
    user_number = int(input("1) Entrez un nombre entre 0 et 5 : "))
    user_lenght_list = user_number - 1

print(number_list)
print(number_list[:user_number])
print(number_list[user_number:])