def Number_Letter_Counts(numb):
    if(len(str(numb)) == 1):
        return telle_enere(numb)
    if(len(str(numb)) == 2 and numb< 20):
        return telle_tenere(numb)
    if((len(str(numb)) == 2 and numb >= 20)):
        return telle_tiere(numb)
    if(len(str(numb)) == 3):
        return telle_hundrere(numb)
    if(len(str(numb)) ==4):
        return len("onethousand")

    

def telle_enere(N):
     enere = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
     return len(enere[N-1])
def telle_tenere(N):
    tenere = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    return len(tenere[N-10])

def telle_tiere(N):
    tiere = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    if((len(str(N)) == 2 and N >= 20) and int(str(N)[1]) == 0):
        return len(tiere[abs(2-int(str(N)[0]))])
    if((len(str(N)) == 2 and N >= 20) and int(str(N)[1]) != 0):
        return len(tiere[abs(2-int(str(N)[0]))]) + telle_enere(int(str(N-1)[1]))
    else:
        return telle_enere(N)
    
def telle_hundrere(N):
    A = len("hundred")
    if((int(str(N)[1])) + int(str(N)[2])) == 0:
        return telle_enere(int(str(N)[0])) + A
    if((int(str(N)[1])) + int(str(N)[2])) != 0:
        if(int(str(N)[1:3]) < 20 and int(str(N)[1:3]) >=10):
            #print("vi er 11 og mer")
            return telle_enere(int(str(N)[0])) + A + telle_tenere(int(str(N)[1:3])) +3
        if(int(str(N)[1:3]) <= 9):
            #print("vi er under 10")
            return telle_enere(int(str(N)[0])) + A + telle_enere(int(str(N)[1:3])) +3
        
        if(int(str(N)[1:3]) >= 20):
            #print(int(str(N)[1:3]))
            return telle_enere(int(str(N)[0])) + A + telle_tiere(int(str(N)[1:3]))+ 3



k = 0
for i in range(1,1001):
   k+= Number_Letter_Counts(i)


print(k)

