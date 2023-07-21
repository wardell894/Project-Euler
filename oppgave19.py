#referanse dato mandag 1900, sjekke forste hver måned deretter

def Die_rata(X):
    mnd_lengde = [31, 28, 31, 30, 31,30,31, 31,30,31,30,31]
    mnd_lengde_skuddar = [31, 29, 31, 30, 31,30,31, 31,30,31,30,31]
    #ant_skuddar  = 0
    K = X-1900
    ant_sondager_forste = 0
    for i in range(1,K+1):
        if(i%4 == 0):
            #ant_skuddar+=1
            Ar = 365*i 
            for L in mnd_lengde_skuddar:
                Ar+=L
                if(Ar%7 == 6):
                    ant_sondager_forste+=1

        if(i%4 != 0):
            Ar = 365*i 
            for L in mnd_lengde:
                Ar+=L
                if(Ar%7 == 6):
                    ant_sondager_forste+=1
    return ant_sondager_forste

print(Die_rata(2000))
