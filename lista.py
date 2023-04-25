Alunos=[]
qnt = int(input("Digite a quantidade de alunos"))

for i in range(qnt):
    Alunos.append(input("Digite o nome dos alunos"))


for P in range(qnt):
    print(P,Alunos[P])