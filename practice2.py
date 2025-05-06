serie = [9, 1, 72, 2, 13, 5]

def minsta_talet(lista):
    minsta = False
    for tal in lista:  
        if minsta == False:
            minsta = tal
        if tal < minsta:
            minsta = tal
    return minsta

def största_talet(lista):
    största = False
    for tal in lista:  
        if största == False:
            största = tal
        if tal > största:
            största = tal
    return största


print(minsta_talet(serie))

print(största_talet(serie))