numero = int(input("Digite um número:"))
cont = 0
total = 0
while numero != 100:
    if (numero > 0) and (numero % 2 == 0):
        cont+= 1
        total+= numero
        valor = total//cont
    else:
        valor = ("Não foram lidos números pares")
    numero = int(input("Digite um número:"))
print(valor)
