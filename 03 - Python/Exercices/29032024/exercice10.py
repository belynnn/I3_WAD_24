# Ennoncé
"""
[v] ● Demandez à l'utilisateur d'entrer des nombre jusqu'à ce qu'il donne la valeur 0.
[v] ● Ensuite, affichez le plus grand et le plus petit nombre que l'utilisateur a donné.
"""

# 1) l'utilisateur entre 4
user_number = int(input("Entrez le bon nombre (0) : "))
correct_number = 0
# 2) affecte 4 à little ET à big
little = big = user_number

while user_number != correct_number :
    # 3) Si 4 est plus petit que 4
    # 9) si 8 est plus petit que 4 ... non
    if user_number < little :
        # 4) petit devient 4
        little = user_number
    # 5) Si 4 est plus grand que 4
    # 10) si 8 est plus grand que 4 vvv
    elif user_number > big :
        # 6) grand devient 4
        # 11) grand devient 8, etc
        big = user_number

    # 7) l'utilisateur entre 8, etc
    user_number = int(input("Entrez le bon nombre (0) : "))
    # 8) user_number devient 8

print(f"Le plus petit nombre est {little}")
print(f"Le plus grand nombre est {big}")