from random import randint

letter_list = ["a", "b", "c", "d", "e", "f"]

random_index = randint(0, len(letter_list) - 1)

print(letter_list)
print(letter_list[random_index])