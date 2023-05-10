num1=int(input("Digite um numero"))
num2=int(input("Digite um numero"))
num3=int(input("Digite um numero"))
if num1 >num2 and num1>num3:
    print("O numero {} é o maior".format(num1))
elif num2> num3:
    print("O numero {} é o maior".format(num2))
else:
    print("o numero {} é o maior".format(num3))