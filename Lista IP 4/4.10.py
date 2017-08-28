quantidade = int(input("Digite a quantidade de kWh consumida:"))
instalação = str.lower(input("Qual o tipo de instalação?"))
R = "residência"
I = "indústria"
C = "comércio"
if instalação == R:
    if quantidade <= 500:
        preço = (quantidade*0.40)
        print("Você pagará R$%s"%(preço))
    else:
        quantidade > 500
        preço = (quantidade*0.65)
        print("Você pagará R$%s"%(preço))
elif instalação == C:
    if quantidade <= 1000:
        preço = (quantidade*0.55)
        print("Você pagará R$%s"%(preço))
    else:
        quantidade > 1000
        preço = (quantidade*0.60)
        print("Você pagará R$%s"%(preço))
else:
    instalação == I
    if quantidade <= 5000:
        preço = (quantidade*0.55)
        print("Você pagará R$%s"%(preço))
    elif quantidade > 5000:
        preço = (quantidade*0.60)
        print("Você pagará R$%s"%(preço)) 
        

    
