ranks  = {"Marie": 1, "Bernard": 4, "François": 2, "Thomas": 12, "Hila": 15}

# V1 - Liste "fictive" de tuple, sera aspiré par le garbage collector, que les autres non car elles sont contenues dans des variables
for name, rank in list(ranks.items()):
    if rank >= 10 :
        ranks.pop(name)

# V2
# to_remove = []
# for name, rank in ranks.items():
#     if rank >= 10:
#         to_remove.append(name)
# for name in to_remove:
#     ranks.pop(name)

# # V3
# clone = {}
# clone.update(ranks)
# for name, rank in clone.items():
#     if ranks >= 10:
#         ranks.pop(name)

average = sum(ranks.values()) / len(ranks)

print(f"Moyenne des meilleurs rangs :\n  ➡️  {average}")