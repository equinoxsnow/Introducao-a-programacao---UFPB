soma = 0
contBom = 0
contRuim = 0
contReg = 0
contEx = 0
media = 0
maiorIdade = 0
x = int(input("Número de pessoas:"))
for c in range(x):
    idade = int(input("Informe sua idade: "))
    opiniao = input("Qual sua opinião sobre o filme? ")
    if (opiniao.lower() == "bom"):
        soma+= idade
        contBom+= 1
    elif (opiniao.lower() == "ruim"):
        contRuim+= 1
    elif (opiniao.lower() == "regular"):
        contReg+= 1
    if(idade > 30):
        if(opiniao.lower() == "excelente"):      
            contEx+= 1
    if (idade > maiorIdade):
        maiorIdade = idade
        contRuimReg = contRuim+contReg
print("A média de idade bom é: {}".format(soma / contBom))
print("A quantidade de respostas ruim/regular é: {}".format(contRuimReg))
print("A quantidade de pessoas acima de 30, que responderam excelente é: {}".format(contEx))
print("A idade da pessoa mais velha é: {}".format(maiorIdade))
