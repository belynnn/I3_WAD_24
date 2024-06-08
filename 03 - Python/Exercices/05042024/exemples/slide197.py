# Le paramètre est la valeur que l'on donne quand on appel la fonction, ici, 5
# Cette valeur de paramètre s'injecte dans l'argument de la fonction définie
# L'argument est une variable que l'on va mettre lorsqu'on définit une fonction, ici, number

def double(number) :
    return number * 2

value = double(int(input("Entrez un nombre : ")))
print(value)