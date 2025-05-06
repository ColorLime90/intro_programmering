''' Vad är sannolikheten att du får yatzy?'''
import random

def kasta_tärningar():
    tärningar = []
    for i in range(5):
        tärningar.append(random.randint(1, 6))
    return tärningar

def kasta_antal_gånger(antal):
    kastserie = []
    for i in range(antal):
        kastserie.append(kasta_tärningar())
    return kastserie

def kolla_för_yatzy(lista):
    for tärning in lista:
        if tärning != lista[0]:
            return False
    return True

def kolla_för_yatzy_kastserie(kastserie):
    antal_false = 0
    antal_true = 0
    for kast in kastserie:
        for tärning in kast:
            if tärning != kast[0]:
                antal_false += 1
                redan_false = True
        if redan_false != True:
            antal_true += 1
        redan_false = False
    return [antal_true, antal_false]
            
def räkna_yatzys():

    print(kolla_för_yatzy([1, 1, 1, 1, 1]))



print(kolla_för_yatzy_kastserie(kasta_antal_gånger(5)))