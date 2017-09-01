numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero1+= 1
cont = 0

if numero1 > numero2:
    numero2,numero1 = numero1,numero2
for c in range(numero1,numero2):
    if (c%4 == 0):
        cont+= 1
print("{} múltiplos".format(cont))
        
