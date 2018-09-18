from random import randint

mazakais = 0
lielakais = 100


while True:
    minejums = randint(mazakais, lielakais)
    print(minejums)
    atbilde = input("Mini no 1 lidz 100, Atbilde ir:")
    if atbilde == "p":
        print("pareizi")
        exit()

    if atbilde == "l":
        mazakais = minejums


    if atbilde == "m":
        lielakais = minejums
        print("turpinam")



