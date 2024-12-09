import random
kortlek_bas = []
antal_kortlekar = 0
kortlek = []
kort_player = []
kort_dealer = []
kort = {}

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

# Tiopotens räknar åt fel håll

def get_sum_of_value_of_cards_in_list(lista):
    sum_tmp = 0
    for objekt in lista:
        sum_kort_tmp = 0
        tiotal = False
        for tecken in objekt:

            
            if tecken.isdigit() == True and tiotal == False:
                sum_kort_tmp = int(tecken)
                tiotal = True
            elif tecken.isdigit() == True:
                sum_tmp = sum_tmp + sum_kort_tmp * 10 + int(tecken)
            sum_tmp = sum_tmp + sum_kort_tmp


    return sum_tmp

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




print(kort_player)

print(len(kortlek))


#Spelet startar:

draw_player(1)
draw_dealer(1)
draw_player(1)
hidden = draw_dealer_hidden(1)

draw_player(input("dra kort"))

print(kort_player)

print(get_sum_of_value_of_cards_in_list(kort_player))