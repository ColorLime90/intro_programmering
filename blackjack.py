import random
kortlek_bas = []
antal_kortlekar = 0
kortlek = []
kort_player = []
kort_dealer = []

# Skapa en kortleksbas  (kortlek_bas)

for l in ("HDSC"):
    for n in range(1, 14):
        kortlek_bas.append(str(l) + str(n))

# Använd kortleksbas för att skapa en aktiv kortlek (kortlek)

antal_kortlekar = int(input("Hur många kortlekar vill du spela med? "))
for i in range(1, antal_kortlekar + 1):
    kortlek.extend(kortlek_bas)

# En funktion för att räkna hur många av ett kort någon har. Används inte

def count_amount(kort, lista):
    count_amount_tmp = 0
    for objekt in lista:
        if objekt == kort:
            count_amount_tmp = count_amount_tmp + 1
    return count_amount_tmp


#   Fel eftersom klädda kort är värda 10
#
#            def get_sum_of_value_of_cards_in_list(lista):      OLD
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


# Output i form av lista där index 0 = summan och index 1 = antal ess

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
    return [sum_tmp, aces]



# x står för antal kort att dra

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


print("Det finns", len(kortlek), "kort i kortleken")


#Spelet startar:

print()
print("Utdelning av kort")
print()

draw_player(1)
draw_dealer(1)
draw_player(1)
hidden = draw_dealer_hidden(1)

print()


if kort_dealer[0] == ("H1" or "S1" or "C1" or "D1"):
    print("Dealern har", len(kort_player) , "kort, och du vet att hen har ett ess")
else:    
    print("Dealern har", len(kort_player) , "kort och du vet att hen har kortet", kort_dealer[0])


player_aces = get_sum_of_value_of_cards_in_list_blackjack(kort_player)[1]
if player_aces == 0:
    print("Du har", len(kort_player) , "kort med summan", get_sum_of_value_of_cards_in_list_blackjack(kort_player)[0])
else:    
    print("Du har", len(kort_player) , "kort med summan", str(get_sum_of_value_of_cards_in_list_blackjack(kort_player)[0]) + ". Du har också", player_aces, "ess.")


print()
