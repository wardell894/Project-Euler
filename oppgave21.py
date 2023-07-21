from math import sqrt
import math
def amicable(K,N):
    amicable = 0
    for i in range(K,N+1,2):
        for j in range(K,N+1,2):
            proper_divisorA = sumPDivisor(i)
            proper_divisorB =  sumPDivisor(j)
            if(proper_divisorA == j and proper_divisorB == i and (i!=sumPDivisor(i))):
                amicable+=i      
        print(i, amicable)
    
    return amicable





def sumPDivisor(N):
    # Note that this loop runs till square root
    i = 1
    divisor_sum = 0
    while i <= math.sqrt(N):
          
        if (N % i == 0) :
              
            # If divisors are equal, print only one
            if (N / i == i) :
                divisor_sum+=i
            else :
                divisor_sum+= (i+int(N/i))
        i = i + 1
    return divisor_sum - N
  
  





print(amicable(210,10*1000))
