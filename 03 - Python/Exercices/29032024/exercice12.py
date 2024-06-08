# Ennoncé
"""
[v] ● Créez un programme qui va demander à l'utilisateur d'entrer des nombres.
[v] ● Le programme continuera à en demander tant que l'utilisateur n'aura pas donné deux nombres identiques d'affilée.
[v] ● En fin de programme, affichez la somme de tous les nombres entrés par l'utilisateur.
# ! réalisé en 30min
"""
# 1) demande au user d'entrer un 1er nombre
previous_number = int(input("Entrez des nombres : "))
# 2) ' nb précédent ' entré est affecté à la somme totale ' sum '
sum = previous_number

# ? 3) tant que ' nb entré ' est != de ' nb suivant '
# while previous_number != next_number :
#     next_number = int(input("Entrez des nombres : "))
#     sum += next_number
# ? 3) on ' continue ' tant que le user n'entre pas 2 nb identique
continuer = True

# 4) TANT QUE ' continuer ' est TRUE (actif)
while continuer :
    # 5) demande au user d'entrer le nb suivant
    next_number = int(input("Entrez des nombres : "))
    # 6) ajoute le nb suivant à la somme total
    sum += next_number

    # 7) si le ' nb suivant ' est == au ' nb précédent '
    if next_number == previous_number :
        # 8) ' continuer ' est FALSE (désactivé)
        continuer = False
    # 9) si nb suivant est autre que ==, ' nb suivant ' est affecté à ' nb précédent ' et continue de boucler tant que ' nb suivant ' est identique à ' nb précédent '
    else :
        previous_number = next_number

# 10) quand la condition de la boucle est remplie, affiche la somme totale de ' sum '
print(f"La somme des nombres entrés est : {sum}")