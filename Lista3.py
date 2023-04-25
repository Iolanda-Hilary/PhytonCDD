nome= []
senha=[]
print("---------Cadastre-se em nossa plataforma!---------")
for i in range(2):

    nome.append(input("Digite seu nome de usuário: "))
    senha.append(input("Digite sua senha: "))
    print("Cadastrado com Sucesso!")

print("==================Efetuando Login========================")

for j in range(2):
    nomelogin=input("Digite novamente seu nome de usuário:")
    senhalogin = input("Digite novamente sua senha:")

    if senhalogin in senha and senhalogin in senha:
        print("{}, Você foi logadx com sucesso!".format(nomelogin))
        break
    else:
        print("Usuário não cadastrado ou senha incorreta, tente novamente!")

