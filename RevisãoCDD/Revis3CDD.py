A=[]
M=[]
X=int(input("Digite mais um numero"))
for Z in range(5):
    A.append(int(input("Digite um numero")))

for Y in range(5):
    M.append(X*A[Y])

print(M)