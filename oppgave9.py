
def Special_Pythagorean_Triplet(A,B,C):
    tester = False
    if(A < B and B < C):
        if(A**2 + B**2 == C**2):
            tester = True
            print(A+B+C)
    return tester


def teste_kombinasjoner(K, Q):
    combo_liste = []
    for i in range(K,Q):
        for j in range(K,Q):
            for k in range(K,Q):
                if(i+j+k == 1000 and Special_Pythagorean_Triplet(i,j,k) == True):
                    print(i,j,k)
                    combo_liste.append([i,j,k])
    print(combo_liste)

#prove seg frem litt
teste_kombinasjoner(200, 500)
