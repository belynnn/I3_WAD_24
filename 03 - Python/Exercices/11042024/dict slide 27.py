scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

pseudo = input("Pseudo : ")
score = input("Score : ")

scores[pseudo] = score

# for key, value in scores.items():
#     print(f"{key} : {value}")

for key, value in scores.items():
    print(f"{key} : {value}")