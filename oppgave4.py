def palindrom_finder():
    palndrom_liste = []
    for i in  range(1,999+1):
        for j in reversed(range(1,999+1)):
         L = i*j
         #print(i,j)
         string_L = str(L)
         if(string_L[::-1] == string_L):
            W = int(string_L)
            palndrom_liste.append(W)

    print(max(palndrom_liste))

    
    

palindrom_finder()
