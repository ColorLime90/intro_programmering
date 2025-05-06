def medelvärde(lista):
    if len(lista) > 0:
        summa = 0
        for tal in lista:
            summa += tal
        return (summa // len(lista))
    else:
        print("error: unvalid list length")

serie_1 = []

inmatning = input("serie_1: ")
while inmatning.isdigit():
    inmatning = int(inmatning)
    serie_1.append(inmatning)
    inmatning = input("serie_1: ")

print(medelvärde(serie_1))