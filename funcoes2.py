def contVogais(T):
    vogais= 'a', 'e', 'i', 'o', 'u','A','E','I','O','U'
    count=0
    for letra in T:
        if letra in vogais:
            count += 1
    print(count)


texto="O rato roeu a roupa do rei de roma"

contVogais(texto)