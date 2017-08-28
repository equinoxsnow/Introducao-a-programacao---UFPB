numero1=int(input("Digite o primeiro valor: "))
numero2=int(input("Digite o segundo valor: "))
cont=0
r=numero1
while numero2 <= r:
    if numero1 == 0 or numero2 == 0 :
        print("Não será possível a divisão")
        break
    else:
        if (numero2 > r):
            print("O resultado da divisão é {} e o resto {}".format(cont,r))         
        else:
            r -= numero2
            cont += 1
print("O resultado da divisão é {} e o resto {}" .format(cont,r))
