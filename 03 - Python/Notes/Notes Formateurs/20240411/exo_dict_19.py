scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

pseudo = input("Votre pseudo: ")
new_score = int(input("Votre score: "))

scores[pseudo] = new_score

print(f"Elocin03 : {scores["Elocin03"]}")
print(f"{pseudo} : {scores[pseudo]}")
