import random
import time
retry = "ja"

while retry == "ja" or retry == "Ja" or retry == "1":
    
    val = input("Dags för sten sax påse! Gör ditt val...  (skriv sten för att välja sten, sax för att välja sax, påse för att välja påse): ")
    if val == "1":
        val = "sten"
    elif val == "2":
        val = "sax"
    elif val == "3":
        val = "påse"

    slumpsiffra = random.randint (1, 3)
    if slumpsiffra == 1:
        slump = "sten"
    elif slumpsiffra == 2:
        slump = "sax"
    elif slumpsiffra == 3:
        slump = "påse"

    print("Du valde", str(val) + ".","Låt oss se om du har turen på din sida...")
    time.sleep(3)
    print("Jag valde", slump)

    if val == "sten" or val == "Sten":
        if slump == "sten":
            print("Det blev lika med sten.")
        elif slump == "sax":
            print("Du vann mot sax!")
        elif slump == "påse":
            print("Du förlorade mot påse...")
    elif val == "sax" or val == "Sax":
        if slump == "sten":
            print("Du förlorade mot sten...")
        elif slump == "sax":
            print("Det blev lika med sax.")
        elif slump == "påse":
            print("Du vann mot påse!")
    elif val == "påse" or val == "Påse":
        if slump == "sten":
            print("Du vann mot sten!")
        elif slump == "sax":
            print("Du förlorade mot sax...")
        elif slump == "påse":
            print("Det blev lika med påse")
    
    retry = str(input("Vill du spela igen? (Ja eller Nej): "))

print("ok ciao")