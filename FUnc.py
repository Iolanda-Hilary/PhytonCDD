def contadordeletras(texto):
    qnt=0
    for letras in texto:
        if texto != ' ':
            qnt += 1
    return len(texto.replace(" ", ""))

quant=contadordeletras()
def textocontrario(texto):
    for x in texto(-1, -quant,-1):
        return texto[x]

texto="iolanda"


print(contadordeletras(texto))

print(textocontrario(texto))

