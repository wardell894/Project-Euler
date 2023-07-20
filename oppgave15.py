import math
"""
https://stemhash.com/counting-lattice-paths/ - og der har vi lært noe nytt
"""
#anta vi alltid starter i punkt (0,0)
def Lattice_Paths(N,K):
    #Binomial koeffisient hvor N = Q =N+K 
    #K = N
    Q =K+N
    return math.comb(Q,K)

print(Lattice_Paths(20,20))
