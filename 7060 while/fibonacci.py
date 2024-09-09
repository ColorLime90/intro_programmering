A = 1
B = 1
N = 1
print("Tal nummer", str(N) + ":", A)
N = N + 1
print("Tal nummer", str(N) + ":", B)
N = N + 1
while N < 30:
    if A > B:
        A = A + B
    else:
        B = A + B
    print()
