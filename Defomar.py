def somar(*numeros):
    tota=0
    for x in numeros:
        tota += x
    return tota

num= somar(2,2,2,2,2,2)

print(num)
