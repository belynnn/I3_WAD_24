ranks ={
    "Marie": 1,
    "Bernard" : 4,
    "François": 2,
    "Thomas": 12,
    "Hila": 15,}

ranks = {name:rank for name, rank in ranks.items() if rank < 10}

avg = sum(ranks.values())
avg /= len(ranks)

print(f"Moyenne des rangs du club: {avg}.")
