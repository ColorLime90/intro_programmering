

def a():
    print("b")

def c():
    return("d")

def e(f):
    return f * f

def i(j):
    print("a", j)

def l(m):
    return"m" + m

def o(p):
    return p + 2

a()

g = c()
print(g)

print(e(3))

i("c")

print(l("o"))

print(o(4))






# lista = ["block 1", 2, "block 3"]

# for x in range(1,5,3):
#    print(x)

# träd = 2
# if isinstance(träd, bool):
#    print("yes")
# else:
#    print("no")

# tal = [2, 4, 6]
# print(tal.index(2))
# tal.append(0)
# print(tal)
'''
lägg talen 2, 3, 2, 4, 1 i en lista
ändra det andra elementet (3) till 5
ändra det sista elementet (1) till 6
Lägg till 4 sist i listan (längst till höger)
beräkna och skriv ut medelvärdet av talen i listan
Sortera listan och skriv ut d
'''
'''
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
'''