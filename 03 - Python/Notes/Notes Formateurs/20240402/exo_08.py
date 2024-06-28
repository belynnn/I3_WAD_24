PASSWORD = "Pyth0n"

password_user = input("Mot de passe: ")
tentatives = 1

while password_user != PASSWORD and tentatives < 3:
    password_user = input("Mot de passe: ")
    tentatives = tentatives + 1

if password_user == PASSWORD:
    print("Mot de passe correct.")
else:
    print("Mot de passe incorrect.")
