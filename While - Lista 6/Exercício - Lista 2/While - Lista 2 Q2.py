cont = 0
qtdadeNumeros = 0
while(cont < 25):
    numero = int(input("Digite um número:"))
    if (numero%2 == 0 and numero > 1):
        qtdadeNumeros+= 1
        cont+= 1
    else:
        cont+= 1
print(qtdadeNumeros)
