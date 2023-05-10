vetor=[]
maior=0
menor=0
soma= 0
for x in range(4):
    vetor.append(int(input("Digite um numero:")))
    soma = 0
contador=0
for y in range(4):
    if vetor[y]%2==0:
        print(vetor[y])
print("===========")

for z in range(4):

     if z == 0:
        maior=vetor[0]
        menor=vetor[0]

     elif maior < vetor[z]:
         maior=vetor[z]
     elif menor > vetor[z]:
        menor=vetor[z]
print(maior, "é o maior vetor")
print(menor, "é o menor vetor")


contador=0
for b in range(4):
    soma= soma+vetor[b]
    divisao=soma/4
    if vetor[b] > divisao:
        contador =+ 1



print(divisao, "É A Media")
print(contador, "numeros sao maiores que a media")







