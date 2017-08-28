salario = float(input("Digite o salário do funcionário:"))
aumento1 = 10/100
aumento2 = 15/100
if salario > 1250.00:
    print(salario*aumento1)
elif salario <= 1250.00:
    print(salario*aumento2)
    
