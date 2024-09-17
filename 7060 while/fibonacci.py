#fick inte isinstance att funka som jag ville. Ville att Programmet skulle funka även om användaren matar in något annat än ett heltal.

A = 1
B = 1
N = 1
antal = int(input("Ange antalet tal i Fibonacci talföljden som ska räknas ut: "))
if isinstance(antal, int):
    antal = int(antal)
    print("Räknar ut", str(antal), "tal")
else:
    antal = 30
    print("Kunde ej läsa värde, räknar ut 30st tal")
print("Tal nummer", str(N) + ":", A)
N = N + 1
print("Tal nummer", str(N) + ":", B)
N = N + 1
while N <= antal:
    if A < B:
        A = A + B
        print("Tal nummer", str(N) + ":", A)
        N = N + 1
    else:
        B = A + B
        print("Tal nummer", str(N) + ":", B)
        N = N + 1