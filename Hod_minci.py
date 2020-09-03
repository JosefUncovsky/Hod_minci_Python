import random
from random import randint
def CoinToss():
    pocet = input("Kolikrát chcete hodit mincí? : ")
    pocet = int(pocet)
    zaznamList = []
    Panna = 0
    Orel = 0
    for amount in range(pocet):
        
        #flips = [randint(0,1) for r in range(pocet)]
        flips = random.randint(0,1)
        if (flips == 1):
            print("Panna")
            zaznamList.append("Panna")
            
        elif(flips == 0):
            print("Orel")
            zaznamList.append("Orel")
            
        print(str(zaznamList))
        print(str(zaznamList.count("Panna")) + " Pan " + str(zaznamList.count("Orel")) + " Orlů")
CoinToss()     
    
