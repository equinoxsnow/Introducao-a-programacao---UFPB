cont = 50
resultado = 0
while(cont > 0):
    numeros = int(input("Digite um número:"))
    if (numeros%3 == 0):
        resultado+= numeros
        cont-= 1
    else:
        cont-= 1
print(resultado)
        
