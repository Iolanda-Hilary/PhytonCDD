escolha="s"
while escolha == "s":
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print("Selecione uma operação: \n 1- soma  \n 2- subtração \n 3- multiplicacao \n 4- divisao \n 5- Reiniciar \n 6- sair")
    resp=input("")

    if resp == "1":
                        soma= n1+n2
                        print(soma)
    elif resp == "2":
                        subtracao= n1-n2
                        print(subtracao)
    elif resp == "3":
                        multiplicacao= n1*n2
                        print(multiplicacao)
    elif resp == "4":
                        divisao=n1/n2
    elif resp == "5":
                      continue
    elif resp == "6":
        print("fim do programa")
        break




