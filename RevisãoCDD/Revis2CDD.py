lista = []
notas = 0
for A in range(4):
    lista.append(float(input("Digite as notas da turma")))
for B in range(4):
    notas = lista[B]+notas
    media = notas/4
print(media)