import random
kortlek_bas = []
antal_kortlekar = ""
kortlek = []

for l in ("HDSC"):
    for n in range(1, 14):
        kortlek_bas.append(str(l) + str(n))
print(kortlek_bas)

antal_kortlekar = int(input("Hur många kortlekar vill du spela med? "))

for i in range(1, antal_kortlekar + 1):
    kortlek.extend(kortlek_bas)

print(kortlek)

def count_amount(x, y):
    count_amount_temp = 0
    for i in y:
        if i == x:
            count_amount_temp = count_amount_temp + 1
    return count_amount_temp


# By default, a module has some hidden variables defined
# print({k: v for k, v in globals().items() if not k.startswith("__")})
#
# for i in range(1, 11):
#    globals()[f"my_variable_{i}"] = i
#
# print()
# print(my_variable_1)
# print(my_variable_2)
# and so on
#
# print()
# print({k: v for k, v in globals().items() if not k.startswith("__")})

def skapa_spelare(x):
    for i in range(1, x + 1):
       spelare = []