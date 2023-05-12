def tnum(t):
    B = []
    for y in t:
        if y not in B:
            B.append(y)
    print(B)


A=[1,2,2,3,4,4,6,6,8,8,8,8,8,19]
tnum(A)