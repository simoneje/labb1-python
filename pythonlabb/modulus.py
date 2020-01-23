def delbartTal():
    listan = []
    for i in range(1,1001):
        if i % 6 == 0 and i % 14 == 0:
            listan.append(i)
    print(listan)    
    print ("Medelvärdet av listan är "+ str(sum(listan)/len(listan)))
    

def gissaTal():
    antalsvar=1
    import random
    right = random.randint(1,100)
    gissa = int(input("Gissa ett tal mellan 1 - 100\n"),10)
    while right != gissa:     
        if gissa < right:
            gissa = int(input("gissa högre\n"),10)
            antalsvar+=1
        elif gissa > right:
            gissa = int(input("gissa lägre\n"),10)
            antalsvar+=1 
    print(f"Bra jobbat, du gissa rätt, det tog dig {antalsvar} försök")
