def erPrimtall(N):
    tester = True
    for i in range(2,N):
        if(N%i==0):
            tester = False
            break
    return [tester, N]


def nth_Prime():
    teller = 2
    prim_tall = []
    while(len(prim_tall) < 10001):
        if(erPrimtall(teller)[0] == True):
            prim_tall.append(teller)
            #print(len(prim_tall))
        teller = teller + 1
    return prim_tall[-1]

print(nth_Prime())
