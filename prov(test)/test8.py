print("Uppgift 1:")
print()

lista = [2, 3, 2, 4, 1]
lista[1] = 5
lista[-1]= 6
lista.append(4)

medel = 0
for a in lista:
    medel = medel + a
medel = medel // len(lista)

lista.append(medel)
lista.sort()
print(lista)


print()
print("Uppgift 2:")
print()


import random
lista1 = []
treor = 0

for i in range(0, 20):
    lista1.append(random.randint(1, 6))
print(lista1)
for i in lista1:
    if i == 3:
        treor = treor + 1
print(treor)
print()