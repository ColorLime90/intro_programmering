#Junk

import random
hjärta = 0
for x in range(0, 4):
    def dra_kort():
        hjärta = random.randrange(1, 13, 1)
    dra_kort()
print(hjärta)