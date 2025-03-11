import os
os.system('cls')

import random
import time
kortlek_bas = []
antal_kortlekar = 1
kortlek = []
kort_player = []
kort_player_stats = []
kort_dealer = []
kort_dealer_stats = []
runda = 0
replay = True
startpengar = 1
pengar = 0
insats = 0

# SKRÄP

""" SKRÄP

#   Fel eftersom klädda kort är värda 10    GAMMAL
#
#            def get_sum_of_value_of_cards_in_list(lista):      GAMMAL
#                sum_tmp = 0
#                for objekt in lista:
#                    sum_kort_tmp = 0
#                    if len(objekt) == 3:
#                        tiotal = True
#                    else:
#                        tiotal = False
#                    lapped = False
#                    for tecken in objekt:
#                        if tecken.isdigit() == True:
#                            if tiotal == True and lapped == False:
#                                sum_kort_tmp = int(tecken)
#                                lapped = True
#                            elif tiotal == True and lapped == True:
#                                sum_kort_tmp = sum_kort_tmp * 10 + int(tecken)
#                            elif tiotal == False:
#                                sum_kort_tmp = int(tecken)               
#                    sum_tmp = sum_tmp + sum_kort_tmp
#                return sum_tmp

# if kort_dealer_stats[0] > 21 and kort_dealer_stats[1] > 0:
#           transform_ace(kort_dealer_stats)
#           draw_dealer()
#           if kort_dealer[int(len(kort_dealer)) - 1] == "H1" or kort_dealer[int(len(kort_dealer)) - 1] == "D1" or kort_dealer[int(len(kort_dealer)) - 1] == "S1" or kort_dealer[int(len(kort_dealer)) - 1] == "C1":
#               kort_dealer_stats[1] = kort_dealer_stats[1] + 1

# lista.append(count_amount("H1", lista) + count_amount("D1", lista) + count_amount("S1", lista) + count_amount("C1", lista))

"""

# FUNKTIONER

# En funktion för att räkna hur många av ett kort någon har. Används inte

def count_amount(kort, lista):
    count_amount_tmp = 0
    for objekt in lista:
        if objekt == kort:
            count_amount_tmp = count_amount_tmp + 1
    return count_amount_tmp

# Output i form av lista där index 0 = summan och index 1 = antal ess.   NOTERA: ANTAL ESS ÄR EGENTLIGEN EFFEKTIVA ESS, OM 21 ÖVERSKRIDS MINSKAR aces MED 1 OCH sum_tmp MINSKAR MED 10.

def get_sum_of_value_of_cards_in_list_blackjack(lista):
    sum_tmp = 0
    aces = 0
    for objekt in lista:
        sum_kort_tmp = 0
        if len(objekt) == 3:
            tiotal = True
        else:
            tiotal = False
        lapped = False
        for tecken in objekt:
            if tecken.isdigit() == True:
                if tiotal == True:
                    sum_kort_tmp = 10
                elif tiotal == False:
                    if int(tecken) == 1:
                        aces = aces + 1
                        sum_kort_tmp = 11
                    else:
                        sum_kort_tmp = int(tecken)               
        sum_tmp = sum_tmp + sum_kort_tmp
    return [int(sum_tmp), int(aces)]

# omvandlar ett ess i en kortlek från 11 till 1, minskar antal ess med 1 och skriver ut antal faktiska ess på index 3   [summa, effektiva ess, antal ess]

def transform_ace(lista):
    if lista[1] > 0:
        lista[0] = lista[0] - 10
        lista[1] = lista[1] - 1
        if len(lista) == 3:
            lista[1] = lista[1] - lista[2]

# x står för antal kort att dra, om inget anges dras 1 kort

def draw_player(x = 1):
    for i in range(1, int(x) + 1):
        kort_drawn_tmp = kortlek.pop(random.randint(0, len(kortlek) - 1))
        kort_player.append(kort_drawn_tmp)
        print("Player fick kortet", kort_drawn_tmp)

def draw_dealer(x = 1):
    for i in range(1, x + 1):
        kort_drawn_tmp = kortlek.pop(random.randint(0, len(kortlek) - 1))
        kort_dealer.append(kort_drawn_tmp)
        print("Dealer fick kortet", kort_drawn_tmp)

def draw_dealer_hidden(x = 1):
    for i in range(1, x + 1):
        kort_drawn_tmp = kortlek.pop(random.randint(0, len(kortlek) - 1))
        kort_dealer.append(kort_drawn_tmp)
        print("Dealer fick ett dolt kort")
        return kort_drawn_tmp

# SETUP

# Skapa en kortleksbas  (kortlek_bas)

for l in ("HDSC"):
    for n in range(1, 14):
        kortlek_bas.append(str(l) + str(n))

print("Inställningar:")
time.sleep(2)
print()

# Använd kortleksbas för att skapa en aktiv kortlek (kortlek)

correct_input = False
while not correct_input:
    antal_kortlekar = input("Hur många kortlekar vill du spela med? ")
    if antal_kortlekar.isdigit():
        antal_kortlekar = int(antal_kortlekar)
        if antal_kortlekar > 0:
            correct_input = True
        else:
            print("Ange ett vettigt nummer.")
    else:
        print("Kunde inte läsa, försök igen.")
    time.sleep(1)
    print()
        
# Inställningar för pengar

correct_input = False
while not correct_input:
    pengar = input("Vill du spela med pengar? (ja, yes, y / nej, no, n) ")
    if pengar == "nej" or pengar == "no" or pengar == "n":
        pengar = False
    else:
        correct_input = False
        while not correct_input:
            startpengar = input("Hur mycket pengar vill du börja med? ")
            if startpengar.isdigit():
                startpengar = int(startpengar)
                if startpengar > 0:
                    pengar = startpengar
                    correct_input = True       
                else:
                    print("Du måste börja med något")
            else:
                print("Kunde inte läsa, försök igen.")
    time.sleep(1)
    print()

os.system('cls')

print("Dags att spela!")
time.sleep(2)
print()

# RUNDA STARTAR

while replay == True:

    kortlek = []
    kort_player = []
    kort_dealer = []


    for i in range(int(antal_kortlekar)):
        kortlek.extend(kortlek_bas)

    runda = runda + 1
    print("Runda", runda)
    time.sleep(2)

    if pengar == False:
        break
    else:
        correct_input = False
        while not correct_input:
            insats = input(f'Hur mycket pengar vill du satsa? (Du har {pengar}) ') 
            if insats.isdigit() == True:
                insats = int(insats)
                if insats >= 0:
                    if insats != 0:
                        if insats <= pengar:
                            correct_input = True
                        else:    
                            print("Du kan inte satsa mer än du har...")
                    else:
                        print("Du måste satsa något :)")
                else:
                    print("Vänligen skriv en positiv summa")
            else:
                print("Vänligen skriv en summa")
            time.sleep(2)
            print()

    print("Det finns", len(kortlek), "kort i kortleken")
    time.sleep(2)
    print()
    print("Utdelning av kort:")
    print()

    time.sleep(1)
    draw_player(1)
    time.sleep(1)
    draw_dealer(1)
    time.sleep(1)
    draw_player(1)
    time.sleep(1)
    draw_dealer_hidden(1)
    time.sleep(1)

    print()
    if kort_dealer[0] == ("H1" or "S1" or "C1" or "D1"):
        print("Dealern har", len(kort_player) , "kort, och du vet att hen har ett ess")
    else:    
        print("Dealern har", len(kort_player) , "kort och du vet att hen har kortet", kort_dealer[0])

    time.sleep(3)
    print()

    # Kolla för ess

    kort_player_stats = get_sum_of_value_of_cards_in_list_blackjack(kort_player)

    if kort_player_stats[1] == 0:
        print("Du har", len(kort_player) , "kort med summan", kort_player_stats[0])
    elif kort_player_stats[1] == 1:
        print("Du har", len(kort_player) , "kort med summan", str(kort_player_stats[0]) + ", varav", str(kort_player_stats[1]), "aktivt ess.")
    else:    
        print("Du har", len(kort_player) , "kort med summan", str(kort_player_stats[0]) + ", varav", str(kort_player_stats[1]), "aktiva ess.")

    time.sleep(3)
    print()

    # Spelaren får välja om hen vill dra mer kort eller inte, funkar ej om spelaren bustat (summa över 21)

    dra_mer_kort = True
    bust = False

    while dra_mer_kort == True and bust == False:

        val = input("Vill du dra ett kort till eller checka? (dra, draw, hit / stå, check, stand) ")

        if val == "dra" or val == "draw" or val == "hit":

            draw_player()
            time.sleep(1)
            print()
            

        elif val == "stå" or val == "check" or val == "stand":

            dra_mer_kort = False

        else:
            print("Kunde inte uppfatta, vänligen skriv igen.")
            print()
            continue


        kort_player_stats = get_sum_of_value_of_cards_in_list_blackjack(kort_player)

        # Om summan är över 21, kolla om spelaren har ess eller om den bustat.

        while kort_player_stats[0] > 21 and bust == False:

            if kort_player_stats[1] == 0:
                bust = True
                print("Du har mer än 21...")
                time.sleep(1)
                break

            elif kort_player_stats[0] > 21 and kort_player_stats[1] > 0:
                transform_ace(kort_player_stats)

        if dra_mer_kort == True and bust == False:
            if kort_player_stats[1] == 0:
                    print("Du har", len(kort_player) , "kort med summan", str(kort_player_stats[0]) + ".")
            else:    
                    print("Du har", len(kort_player) , "kort med summan", str(kort_player_stats[0]) + ". Du har också", kort_player_stats[1], "aktiva ess.")
            time.sleep(3)

    time.sleep(1)
    print()

    kort_dealer_stats = get_sum_of_value_of_cards_in_list_blackjack(kort_dealer)

    if bust == True:

        vinst = False

    else:

        # Om dealern vinner utan att dra kort:

        if kort_dealer_stats[0] > kort_player_stats[0] and kort_dealer_stats[0] >= 17 and kort_dealer_stats[0] <= 21:

            print("Dealern hade förutom kortet", str(kort_dealer[0]), "också kortet", str(kort_dealer[1]), "med summan", str(kort_dealer_stats[0]) + ", vilket blir mer än summan av dina kort:", str(kort_player_stats[0]))
            time.sleep(3)
            dra_mer_kort_dealer = False
            vinst = False

        elif kort_dealer_stats[0] == kort_player_stats[0] and kort_dealer_stats[0] >= 17:
            print("Dealern hade förutom kortet", str(kort_dealer[0]), "också kortet", str(kort_dealer[1]), "med summan", str(kort_dealer_stats[0]) + ", vilket blir lika mycket som dina kort.")
            time.sleep(3)
            vinst = "lika"
            dra_mer_kort_dealer = False

        else:
            print("Dealern hade förutom kortet", str(kort_dealer[0]), "också kortet", str(kort_dealer[1]), "med summan", str(kort_dealer_stats[0]))
            time.sleep(3)
            dra_mer_kort_dealer = True


        # Om dealern behöver dra mer kort: 

        while dra_mer_kort_dealer == True:
            
            kort_dealer_stats = get_sum_of_value_of_cards_in_list_blackjack(kort_dealer)

            # Kolla om dealern har för mycket.

            while kort_dealer_stats[0] > 21:

                if kort_dealer_stats[1] == 0:
                    dra_mer_kort_dealer = False
                    print("Dealern bustade en hård nöt.")
                    time.sleep(1)
                    vinst = True
                    break

                elif kort_dealer_stats[1] > 0:
                    transform_ace(kort_dealer_stats)
                    print("Dealerns ess omvandlas till 1")
            
            if kort_dealer_stats[0] < 17:
                print("Dealern behöver dra ett till kort")
                time.sleep(2)
                draw_dealer()
                time.sleep(3)
            else:
                dra_mer_kort_dealer = False

        if kort_dealer_stats[0] > kort_player_stats[0] and kort_dealer_stats[0] >= 17 and kort_dealer_stats[0] <= 21:
            print("Dealern har mer än dig. (" + str(kort_dealer_stats[0]) + ")")
            time.sleep(2)
            vinst = False

        elif kort_dealer_stats[0] == kort_player_stats[0] and kort_dealer_stats[0] >= 17:
            print("Du och dealern har lika mycket")
            time.sleep(2)
            vinst = "lika"

        else:
            print("Du har mer än dealern; som har", kort_dealer_stats[0])
            time.sleep(2)
            vinst = True    

    # RESULTAT        

    if pengar == False:
        if vinst == False:
            print("Du förlorade ):")
        elif vinst == True:
            print("Du vann!")
        elif vinst == "lika":
            print("Det blev lika.")
    else:
        if vinst == False:
            print("Du förlorade ):")
            pengar = pengar - insats
        elif vinst == True:
            print("Du vann!")
            pengar = pengar + insats
        elif vinst == "lika":
            print("Det blev lika.")

    time.sleep(3)

    print()
    print("Spelstatistik:")
    print("Spelarens kort:", kort_player)
    print("Kortsumma spelare:", kort_player_stats[0])
    print()
    print("Dealerns kort:", kort_dealer)
    print("Kortsumma dealer:", kort_dealer_stats[0])
    print()
    if pengar != False:
        print("Pengar:", pengar)
        print("Netto:", pengar - startpengar)
        print()

    time.sleep(3)

    if pengar != 0 or pengar == False:

        replay = input("Spela igen? (nej, no, n / ja, japp, jajamänsan, absolut, nu kör vi, gurka) ")
        if replay == "nej" or replay == "no" or replay == "False" or replay == "n":
            replay = False
        else:
            replay = True
    
    else:
        print("Du har tyvärr slut på pengar. Ditt äventyr slutar här. Bra spelat! (inte)")
        replay = False