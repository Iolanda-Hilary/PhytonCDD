count1= 0
count2= 0
for x in range(10):

    numero= int(input("Digite um numero"))

    if numero >=10 and numero<=20:
        count1 = count1 + 1

    else:
        count2 = count2 + 1

print(count1,"numeros estao dentro do intervalo entre 10 e 20")
print(count2, "numeros estao fora do intervalo")
