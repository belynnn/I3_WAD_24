# def sum_elements_table(list) :
#     total = 0
#     for line in range(len(list)) :
#         subtotal = 0
#         for column in range(len(list[line])) :
#             subtotal += list[line][column]
#         total += subtotal

#     print(total)

# number_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# sum_elements_table(number_table)
# addition + multiplication = associatif ? c'est les parenthèses, on peut mettre plein de parenthèse ou les enlever ça ne change rien au calcul
# a = 1+ 2 + 3 - 4 - 5 - 6
# la soustraction n'est pas associative
# commutatif

# CORRECTION
def sum_list(table) :
    sum_numbers = 0

    for line in table :
        for value in line :
            sum_numbers += value

    print(sum_numbers)

num_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum_list(num_table)