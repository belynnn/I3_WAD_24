scores = {"Marie": 1, "Bernard": 4, "François": 2, "Thomas": 12, "Hila": 15}

total = sum(scores.values())
nb_player = len(scores)
moyenne = total / nb_player

print(f"\nSomme totale :\n ---> {total}")
print(f"Moyenne :\n ---> {moyenne}")


# CORRECTION
ranks = {
    "Marie"     : 1, 
    "Bernard"   : 4, 
    "François"  : 2, 
    "Thomas"    : 12, 
    "Bloup"    : 54, 
    "Hila"      : 15}
# V1
# average = sum(ranks.values())
# average /= len(ranks)

# print(f"Moyenne des rangs du club : {average}")

#V2
sum_rank = 0
for rank in ranks.values():
    sum_rank += rank

average = sum_rank / len(ranks)

print(f"Moyenne des rangs du club : {average}")

# TROUVER LA MEDIANE
ranks_values = list(ranks.values())
ranks_values.sort()

print(ranks_values)

nb_players = len(ranks_values) // 2

if len(ranks_values) % 2 == 0:
    median = ranks_values[nb_players-1:nb_players+1]
else:
    median = ranks_values[nb_players]

print(f"Médiane : {median}")