scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

pseudo = input("Pseudo : ")
score = input("Score : ")

scores[pseudo] = score

print(scores)
print(f"Le score d'Elocin03 est {scores["Elocin03"]}")
print(f"Le score de {pseudo} est {scores[pseudo]}")