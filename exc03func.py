def Produto(quantidade,valunit):
    valtotal=quantidade*valunit
    return valtotal

quantidade=int(input("quantidade em estoque:"))
valunit=float(input("valor unitario:"))

valortotalvariavel= Produto(quantidade,valunit)

conta=valortotalvariavel - 1
print(conta)