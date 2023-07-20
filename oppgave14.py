def collatz_Sequence(N):
    len_sec = 1
    while(N > 1):
        #print(N)
        if(N%2 == 0):
            N = int(N/2)
            len_sec+=1
        else:
            N = int(3*N +1)
            len_sec+=1
        #if(N==1):
    return len_sec


def Longest_Collatz_Sequence(N):
    lengste_sek = 0
    while(N>1):
        if(collatz_Sequence(N) > lengste_sek):
            lengste_sek = collatz_Sequence(N)
            print(lengste_sek, N)
        N = N-1

    return lengste_sek


print(Longest_Collatz_Sequence(1000000))
#print(collatz_Sequence(837799))
