resp="s"
lista=[]
while resp== "S" or resp=="s":
    nota1=float(input("digite a nota1"))
    nota2=float(input("digite a nota2"))

    media= (nota1 + nota2)/2
    lista.append(media)
    print(media)

    if media >= 7:
            print("você esta aprovado")
    elif media >=4:
            print("Você esta de recuperação")
    else:
            print("Você reprovou!")
    resp = input("Deseja calcular a media novamente?")
print(lista)


