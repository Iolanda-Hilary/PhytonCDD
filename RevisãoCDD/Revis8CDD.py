MacaComprada=int(input("Digite quantidade de maçãs compradas"))

if MacaComprada < 12:
    maca=1.30
    total=maca*MacaComprada
    print(f"voce gastou{total} em maçãs")
elif MacaComprada >= 12:
    maca=1.00
    total=maca*MacaComprada
    print(f"voce gastou {total} em maçãs com desconto")