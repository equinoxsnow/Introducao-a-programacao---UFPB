valorcasa = float(input("Digite o valor da casa:"))
sal = float(input("Digite o valor do salário:"))
anos = int(input("Digite a quantidade de anos a pagar:"))
prestmen = (valorcasa/(anos*12))
if prestmen >= (sal*0.30):
    print("Seu empréstimo foi negado!")
elif prestmen < (sal*0.30):
     print("Seu empréstimo foi aceito!")
    
