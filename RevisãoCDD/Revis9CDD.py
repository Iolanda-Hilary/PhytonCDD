array=[]
lista=[]
for x in range(5):
    array.append(int(input("Digite numeros para alimentar o array")))
for y in range(5-1,-1,-1):
    lista.append(array[y])

print(lista)