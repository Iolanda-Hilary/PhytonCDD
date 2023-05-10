from Funcoes import *

resp=0
while resp == 0:
    resp=int(input("que operação deseja realizar? \n 1- Somar \n 2-Subtrair \n 3-Multiplicar \n 4-Dividir \n 5-Sair -"))

    if resp == 5:
        break

    n1 = int(input("Digite o primeiro numero"))
    n2 = int(input("Digite o segundo numero"))

    if resp == 2:
           subtrair(n1,n2)
    elif resp == 3:
           multiplicar(n1,n2)
    elif resp == 4:
            dividir(n1,n2)
    elif resp == 1:
            somar(n1,n2)

    resp=0