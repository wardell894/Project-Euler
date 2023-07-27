import pandas as pd
A=pd.read_csv("https://projecteuler.net/resources/documents/0022_names.txt", sep ="\t")
A = str(A).split(",")
A = list(map(lambda x: x[1:-1], A))
A[-1] = "ALONSO"
A[0] = "MARY"
A.sort(key=lambda x:x)
#W =sum(list(map(lambda x: (ord(x) - 64), A[937])))
#print(W)

def Numerisk_Verdi_navn(navn, indeks):
    value_name =sum(list(map(lambda x: (ord(x) - 64), navn)))
    return value_name * (indeks+1)

def svaret():
    return sum(list(map(lambda x: Numerisk_Verdi_navn(x, A.index(x)), A)))

print(svaret())

