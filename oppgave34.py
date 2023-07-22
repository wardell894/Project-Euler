import numpy as np
def digit_factorial(N):
    A = list(str(N))
    A_sum = sum(list(map(lambda x: np.math.factorial(int(x)), A)))
    if(A_sum == N):
        return True


def svaret():
    teller = 0
    for i in range(3,146*10000):
        if(digit_factorial(i) == True):
            teller+=i
    return teller


print(svaret())
