senha = 123
valor = int(input("Digite sua senha"))
tentativas = 1
while senha != valor:
    if tentativas <= 3:
        novamente =  int(input("Digite novamente sua senha"))
        tentativas = tentativas +1

    print("conta bloqueada")
