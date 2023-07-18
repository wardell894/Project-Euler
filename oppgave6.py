def Sum_Square_Difference(N):
    n_forste = int(N*(N+1)/2)
    n_forste_squared = n_forste**2
    n_squared = 0
    for i in range(N+1):
        n_squared += i**2
    #print(n_squared)
    svaret = n_forste_squared - n_squared
    return svaret


print(Sum_Square_Difference(100))
