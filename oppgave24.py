import itertools
from functools import reduce
def losning():
    A = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
    F = list((A[1000001]))
    losning = reduce(lambda y,z:str(y)+str(z), F)
    return int(losning)

print(losning())
