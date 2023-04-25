A=[]
for i in range(5):
    A.append((int(input("Digite um numero"))))
X=int(input("Digite o numero multiplicador"))

M=[]
for j in range(5):
    M.append(X*A[j])
print(M)
