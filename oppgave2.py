# importerer numoy
import numpy as np

# definerer funksjonen
def fibbonaci(N):
    #lager t
    x = np.zeros(N+1, int)
    #setter de første verdiene til 1
    x[0] = 1
    x[1] = 1
    even_list = []
    # følger formelen som gitt
    for k in range(1,N+1):
        x[k] = x[k-1]+ x[k-2]
        #print(k,x[k])
        if(x[k]%2 == 0):
            even_list.append(x[k])
    return even_list


print(sum(fibbonaci(32)))
