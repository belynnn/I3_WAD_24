"""
[v] Récupérez un nombre au clavier et stockez-le dans une variable.
[v] Si le nombre récupéré est plus grand ou égale à 10 affichez “Bravo!”.
[v] Sinon, si il est plus grand que 8 affichez “Pas mal.”
[v] Sinon, si le nombre est plus grand que 5 affichez “Mouais, bof”
[v] Et sinon dans les autres cas affichez “Pas terrible”
"""

number = int(input("Entrez un nombre entre 0 et 10 : "))

# Si le nombre récupéré est plus grand ou égale à 10 affichez “Bravo!”.
if number >= 10 :
    print("Bravo!")
# Sinon, si il est plus grand que 8 affichez “Pas mal.”
elif number > 8 :
    print("Pas mal.")
# Sinon, si le nombre est plus grand que 5 affichez “Mouais, bof”
elif number > 5 :
    print("Mouais, bof")
# Et sinon dans les autres cas affichez “Pas terrible”
else :
    print("Pas terrible")