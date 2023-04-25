tam=int(input("Digite o tamanho dos vetores"))
A=[]
B=[]
C=[]
for i in range(tam):
    A.append(int(input("Digite o primeiro valor")))
    B.append(int(input("Digite o segundo valor")))
for j in range(tam):
    C.append(A[j] + B[j])

print(C)