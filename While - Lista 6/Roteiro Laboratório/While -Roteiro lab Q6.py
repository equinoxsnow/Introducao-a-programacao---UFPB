cont = True
while (cont):
    numero = int(input("Digite um número:"))
    numero2 = int(input("Digite um número:"))
    if (numero <= 0) or (numero2 <= 0):
        print((numero+numero2)/2)
    else:
        print((numero+numero2),(numero*numero2))
    pergunta = input("Deseja continuar[S/N]?").upper()
    if pergunta == "N":
        cont = False
        
