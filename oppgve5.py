def antall_faktorer(N):
    if(N< 2520):
        return 0
    ant_faktorer = 0
    for i in range(1,20):
        k = N%i
        if(k == 0):
            ant_faktorer += 1
    return [ant_faktorer, N]

def smallest_multiple():
    svaret = [1,1]
    teller = 362880000
    ant_liste = []
    while(svaret != 0 and svaret[0] !=20):
        svaret = antall_faktorer(teller)
        if(svaret != 0 and svaret[0] > 18):
            ant_liste.append(svaret[1])
        teller -= 20
    return min(ant_liste)
        
print(smallest_multiple())
