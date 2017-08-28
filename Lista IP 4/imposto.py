salario = float(input("Digite seu salário:"))
imposto1 = 17/100
imposto2 = 8/100
imp1 = (salario * imposto1)
imp2 = (salario * imposto2)
if salario >= 1000:
    salario*imposto1
    print ("O valor pago de impostos foi: R$%2.2s" %(imp1))
else:
    salario*imposto2
    print ("O valor pago de impostos foi: R$%2.2s" %(imp2))
