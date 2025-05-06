serie = [9, 1, 72, 2, 13, 5, 52, 87]

def räkna_över_gräns(lista, gräns):
    antal = 0
    for tal in lista:
        if tal >= gräns:
            antal += 1
    return antal

print(räkna_över_gräns(serie, 50))