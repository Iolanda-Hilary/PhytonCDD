resp="s"
while resp=="s":
    num1=float(input("Digite um numero"))

    if num1 != 0:
            if num1 >0:
                print("Numero Positivo")
            else:
                print("Numero Negativo")
    else:
        num1=float(input("Digite um numero válido"))

    resp=input("Deseja continuar?")