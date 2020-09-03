#Autor: Josef Unčovský
#Datum: 03-09-2020
#Popis: Funkce simulující hod mincí
import random
from random import randint
def CoinToss():
    pocet = input("Kolikrát chcete hodit mincí? : ")
    pocet = int(pocet)
    zaznamList = []
    Panna = 0
    Orel = 0
    for amount in range(pocet):
        
        
        hod = random.randint(0,1)
        if (hod == 1):
            print("Panna")
            zaznamList.append("Panna")
            
        elif(hod == 0):
            print("Orel")
            zaznamList.append("Orel")
            
        print(str(zaznamList))
        print(str(zaznamList.count("Panna")) + " Panen " + str(zaznamList.count("Orel")) + " Orlů")
CoinToss()     
    
