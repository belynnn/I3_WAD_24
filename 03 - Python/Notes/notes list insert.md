numbers = [2, 3, 5, 7, 11, 13]

# insérer à l'index 1
numbers.insert(1, 'X')

# insérer avant dernier
numbers.insert(-1, 'X')

# insérer à la fin
numbers.insert(len(numbers), 'X')
# OU !!! à privilégier
numbers.append('X')

# insérer début
numbers.insert(0, 'X')

print(numbers)