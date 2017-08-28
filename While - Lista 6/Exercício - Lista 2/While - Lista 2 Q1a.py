cont = 20
soma = 0
while (cont > 0):
    cont-=1
    numero = int(input("Digite um número:"))
    if (numero % 2 == 0):
        soma+= numero
print(soma)
