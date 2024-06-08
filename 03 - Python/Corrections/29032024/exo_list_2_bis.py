elements = ["fire", "water", "air", "earth", "metal", "wood"]

index = -1

while index < 0 or index >= len(elements):
    index = input("index: ")
    index = int(index)

print(elements)
print(elements[:index])
print(elements[index:])