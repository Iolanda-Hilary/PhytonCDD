tam=int(input("Digite o tamanho do vetor"))
vetor=[]
contador=0
for x in range(tam):
    vetor.append(int(input("Digite um numero: ")))

num=int(input("Digite o numero a ser procurado:"))
for y in range(tam):

  if num == vetor[y]:
    contador+= 1

print(contador)