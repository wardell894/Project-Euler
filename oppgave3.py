#her var jeg såpass frekk og gikk bare for oddetall istedenfor heleveien for å finne primtallsfaktorer
from functools import reduce
def largest_prime_factor(N, F):
    faktor_liste = []
    for i in range(1,N):
        K = 2*i+1
        if (F%K == 0):
            print(K)
            faktor_liste.append(K)
    result1 = reduce((lambda x, y: x * y), faktor_liste)
    return result1
print(largest_prime_factor(10000, 600851475143))
#print(71*839*1471*6857)
print(600851475143)
