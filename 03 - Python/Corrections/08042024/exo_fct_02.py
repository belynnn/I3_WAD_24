def sum_list(table):

    sum_numbers = 0

    for line in table:
        for value in line:
            sum_numbers += value

    print(sum_numbers)


# -- main program --

num_table = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]] # --> 78

print(sum(num_table))
sum_list(num_table)