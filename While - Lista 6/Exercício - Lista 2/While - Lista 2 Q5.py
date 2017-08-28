cont = True
quantidade = 0
while(cont):
    idade = int(input("Digite a idade:"))
    if(idade >=3) and (idade<=6):
        quantidade+= 1
    pergunta = input("Deseja continuar[S/N]?").upper()
    if pergunta == "N":
        cont = False
print(quantidade)

    
