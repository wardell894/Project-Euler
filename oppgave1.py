def multiples_3_5(N):
    k = 0 
    for i in range(N):
        if(i%3 == 0):
            k+= i
        if(i%5 == 0):
            k+= i
        if(i%15 == 0):
            k -=i
            
    
    return k



print(multiples_3_5(1000))
