from random import randint

# def say_hello() :
#     salutations = ["Bonjour", "Hello", "Ola", "Aloha", "Dag", "Ohayo", "Annyong"]

#     for i in range(len(salutations)):
#         index = randint(0, len(salutations) - 1)
#     print(salutations[index])

# for i in range(100) :
#     say_hello()



####################################
# CORRECTION                       #
####################################
def greetings() :
    possibilities = ["Bonjour", "Hello", "Ola", "Aloha", "Dag", "Ohayo", "Annyong"]

    index = randint(0, len(possibilities) - 1)
    
    print(possibilities[index])

for _ in range(100) :
    greetings()