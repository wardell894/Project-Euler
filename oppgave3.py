from functools import reduce
def largest_prime_factor(N, F):
    faktor_liste = []
    for i in range(1,N):
        K = 2*i+1
        if (F%K == 0 and erPrimtall(K) == True):
            faktor_liste.append(K)
    return max( faktor_liste)

def erPrimtall(N):
    for i in range(2,N):
        tester = True
        if(N%i==0):
            tester = False
            break
    return tester
     
       
print(largest_prime_factor(10000, 600851475143))
