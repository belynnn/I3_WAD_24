scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

pseudo = input("Pseudo: ")
score = input("Score: ")
score = int(score)

scores[pseudo] = score

for item in scores.items():
    print(f"{pseudo}: {score}")