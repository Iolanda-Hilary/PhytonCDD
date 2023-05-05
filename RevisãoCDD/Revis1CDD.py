nomes=[]
for x in range(3):
    nomes.append(input("Digite o nome do aluno"))
for y in range(3):
     print(y,nomes[y])

for t in range(3):
    aluno=input("Digite o nome do aluno para procurar")

    if aluno in nomes:
        print("aluno encontrado na posição {}".format(t))
    else:
        print("Aluno não consta")



