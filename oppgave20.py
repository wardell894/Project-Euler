import math 
from functools import reduce
A = list(str((math.factorial(100))))
A_Svar = reduce((lambda x, y: int(x) + int(y)), A)
print(A_Svar)
