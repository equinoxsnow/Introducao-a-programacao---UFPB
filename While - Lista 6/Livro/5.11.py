deposito=float(input("Digite o valor do depósito inicial: "))
juros=float(input("Digite a taxa de juros: "))
jurosfinal= juros/100
x=0

while x < 24:

    res= (deposito * jurosfinal) + deposito
    deposito = res
    x +=1
    valorfinal = res
    print("{} mês = " .format(x),end="")
    print("R$ {:.2f}".format(valorfinal))
  
