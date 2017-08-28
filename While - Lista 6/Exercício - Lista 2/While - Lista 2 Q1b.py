cont = 30
qtdePositivos = 0
numero = int(input())
while (cont > 0):
    if (numero > 0):
        qtdePositivos+= 1
    cont-= 1
    numero = int(input())
print(qtdePositivos)
