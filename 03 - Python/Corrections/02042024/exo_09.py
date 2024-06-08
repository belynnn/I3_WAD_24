from random import randint


n1 = randint(1, 6)
n2 = randint(1, 6)
n3 = randint(1, 6)

print(str(n1) +  " - " + str(n2) + " - " + str(n3))

while n1 != n2 or n2 != n3:
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    n3 = randint(1, 6)

    print(str(n1) +  " - " + str(n2) + " - " + str(n3))