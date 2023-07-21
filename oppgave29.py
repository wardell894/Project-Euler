def distinct_powers(A,B):
    K = []
    for i in range(A,B+1):
        for j in reversed(range(A,B+1)):
            K.append(i**j)
    
    return len(set(K))


print(distinct_powers(2,100))
