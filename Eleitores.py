
votosBrancos=int(input("Digite quantos votos brancos"))
votosNulos=int(input("Digite quantos votos nulos"))
votosValidos=int(input("Digite quantos votos validos"))

votosTotais=votosNulos+votosValidos+votosBrancos

percentualBrancos=(votosBrancos*votosTotais)/100
print(percentualBrancos, "% de votos brancos")
percentualNulos=(votosNulos*votosTotais)/100
print(percentualNulos, "% de votos Nulos")
percentualValidos=(votosValidos*votosTotais)/100
print(votosValidos, "% de votos Válidos")
print("=======================================")
print(votosTotais, "pessoas votaram ")






