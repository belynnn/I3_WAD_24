ranks ={
    "Marie": 1,
    "Bernard" : 4,
    "François": 2,
    "Thomas": 12,
    "Hila": 15,}

sum_rank = 0

for rank in ranks.values():
    sum_rank += rank

avg = sum_rank /len(ranks)

print(f"Moyenne des rangs du club: {avg}.")
