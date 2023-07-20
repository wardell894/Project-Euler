from functools import reduce
def Power_Digit_Sum(power):
    numb = 2**power
    numb = list(str(numb))
    #print(numb)
    return reduce((lambda x, y: int(x) + int(y)), numb)

print(Power_Digit_Sum(1000))
