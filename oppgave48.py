from functools import reduce
def self_powers(N):
    teller = 1
    self_power_sum = 0
    while(teller <N):
        self_power_sum += teller**teller
        teller+=1
    
    A = list(str(self_power_sum))
    svaret = reduce(lambda x,y:str(x)+str(y), A[len(A)-10:])
    return svaret

print(self_powers(1000))
