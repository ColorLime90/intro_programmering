import random

antalkast = 0
antalvinster = 0
antalförluster = 0
checkjackpot = False

while checkjackpot == False:
    antalkast = antalkast + 1
    tärning1 = random.randint(1,6)
    tärning2 = random.randint(1,6)
    print("Försök nummer", str(antalkast) + ":", "första tärning:", tärning1, "andra tärning:", tärning2)
    if tärning1 == tärning2:
        if tärning1 == 6:
            print("Jackpot!")
            checkjackpot = True
        else:
            print("You win!")
            antalvinster = antalvinster + 1
    else:
        print("you lose ):")
        antalförluster = antalförluster + 1
if antalkast == 1:
    print("Du fick en jackpot på första försöket! Imponerande...")
elif antalkast > 1 and antalvinster == 1:
    print("Du behövde", antalkast, "kasttillfällen för att få en jackpot, därav ett kast var en vanlig vinst...")
elif antalkast > 1 and antalvinster == 0:
    print("Du behövde", antalkast, "kasttillfällen för att få en jackpot. Innan dess fick du inga vanliga vinster...")
else:    
    print("Du behövde", antalkast, "kasttillfällen för att få en jackpot, därav", antalvinster, "av kasten blev vanliga vinster...")