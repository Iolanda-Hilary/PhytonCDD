notas=[]
for i in range(5):
    notas.append(float(input("Digite a nota do alunos{}".format(i))))

contador=0
for j in notas:
   contador=contador+j
   media=contador/5

print(media)
aprovados = 0
for k in notas:
    if k > media:
        aprovados = aprovados +1
print("{} alunos Aprovados".format(aprovados))


