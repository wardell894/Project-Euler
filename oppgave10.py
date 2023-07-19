#kanskje internetts tregeste løsning. prøve algoritmen til dave når får tid
def erPrimtall(N):
    tester = True
    for i in range(2,N):
        if(N%i==0):
            tester = False
            break
    return tester

def prim_tall_sum():  
    primtall_sum = 2
    oddetall = 1
    for i in range(1,999999+1):
        oddetall = 2*i +1
        if(erPrimtall(oddetall) == True):
            primtall_sum += oddetall
        print(i)

    return primtall_sum

print(prim_tall_sum())
