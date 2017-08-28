valor = float(input("Digite  o valor do produto comprado:"))
formaPagamento = str.lower(input("Digite a forma de pagamento!"))
valorTotal = 0

if (valor >= 100) and (formaPagamento == "dinheiro"):
    desconto = (valor*0.1)
    valorTotal = valor-desconto
    print(valorTotal)
elif (valor <100)and(formaPagamento == "dinheiro"):
    valorTotal = valor
    print(valorTotal)
elif (formaPagamento == "cheque"):
    valorTotal = valor
    print(valorTotal)
else:
    print("Forma de pagamento inválida")

