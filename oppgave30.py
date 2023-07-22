def fifth_power():
    fifth_power_liste = []
    for i in range(2,10000000):
        K = list(str(i))
        if(len(K) >= 2):
            K_Sum = sum(list(map(lambda x: int(x)**5, K)))
            if(i == K_Sum):
                fifth_power_liste.append(i)
    
    return sum((fifth_power_liste))

print(fifth_power())
