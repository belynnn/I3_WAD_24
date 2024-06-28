ranks ={
    "Marie": 1,
    "Bernard" : 4,
    "François": 2,
    "Thomas": 12,
    "Hila": 15,
    "Charifa": 25}

rank_values = list(ranks.values())
rank_values.sort()

n = len(rank_values) // 2

if len(rank_values) % 2 == 0:
    median = rank_values[n - 1: n + 1]
else:
    median = rank_values[n]

print(f"Notre médian est de : {median}")