# password = input("Mot de passe: ")
# if password != "Pyth0n":
#     print("Code erroné")
#     password = input("Ré-essayez: ")
#     if password == "Pyth0n":
#         print("Ah ben voilà...")
#     else:
#         print("Bon vraiment pas.")
# else:
#     print("Code valide")

a = 3
if a < 10:
    print("Message 1 < 10")
    a = 300
elif a < 100:
    print("Message 2 entre 10 et 100")
elif a < 1000:
    print("Message 3 entre 100 et 1000")
else:
    print("Message 4 > 1000")

print("End!")
print(a)