cont = 0
while cont < 4:
    cont+=1
    numero = int(input("Digite um n�mero:"))
    numero2 = int(input("Digite um n�mero:"))
    if (numero <= 0) or (numero2 <= 0):
        print((numero+numero2)/2)
    else:
        print((numero+numero2),(numero*numero2))
