import math
def generere_nte_triangular_numbers(N):
    S = int(N*(N+1)/2)
    return S
"""
def antall_divisorer(N):
    divisorer = 0
    for i in range(1,N+1):
        if(N%i == 0):
            divisorer+=1
            #print(divisorer)
    return divisorer
"""

def antall_divisorer(n) :
      
    i = 1
    divisorer = 0
    while i <= math.sqrt(n):
          
        if (n % i == 0) :
            if (n / i == i) :
                divisorer +=1
            else :
                divisorer+=2
        i+=1
    return divisorer
  



def Highly_Divisible_Triangular_Number():
    teller = 1
    while(antall_divisorer(generere_nte_triangular_numbers(teller)) < 500):
        teller+=1
    return generere_nte_triangular_numbers(teller)

print(Highly_Divisible_Triangular_Number())



