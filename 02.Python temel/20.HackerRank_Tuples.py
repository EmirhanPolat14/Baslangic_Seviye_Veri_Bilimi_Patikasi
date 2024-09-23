a = input()
b = input()

liste = []

for i in b.split():
    liste.append(int(i))

t = tuple(liste)

print(hash(t))




    