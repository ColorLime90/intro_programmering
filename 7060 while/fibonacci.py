A = 1
B = 1
N = 1
antal = input("Ange antalet tal i Fibonacci talföljden att räkna ut")
print("Räknar ut", antal, "tal")
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