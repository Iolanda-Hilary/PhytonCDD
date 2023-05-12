def Produto(quantidade,valunit, nome):
    valtotal=quantidade*valunit
    return nome, valtotal #forma e retorna a tupla com a respectivas posições

#quantidade=int(input("quantidade em estoque:"))
#valunit=float(input("valor unitario:"))

nome,preco=Produto(3, 4.50, "carne")

print(f"o produto",preco,"custa", nome)
