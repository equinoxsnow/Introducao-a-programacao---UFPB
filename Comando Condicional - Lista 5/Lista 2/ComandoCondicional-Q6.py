valor = float(input("Digite  o valor do produto comprado:"))
formaPagamento = str.lower(input("Digite a forma de pagamento:"))
valorTotal = 0

if (valor >= 100) and (formaPagamento == "dinheiro"):
    desconto = (valor*0.1)
    valorTotal = valor-desconto
    print("O valor comprado deu {} R$".format(valorTotal))
elif (valor <100)and(formaPagamento == "dinheiro"):
    valorTotal = valor
    print("O valor comprado deu {} R$".format(valorTotal))
elif (formaPagamento == "cheque"):
    valorTotal = valor
    print("O valor comprado deu {} R$".format(valorTotal))
elif (formaPagamento == "cartão"):
   opcao = str.lower (input("Crédito ou Débito?"))
   if (opcao == "crédito"):
       parcela = int(input("Parcela em quantas vezes?"))
       parcelamento = valor / parcela
       if(parcela > 3):
           print("Erro! Você não pode parcelar mais que 3 vezes")
       else:
           print("Vão ser {} parcelas de {}".format(parcela, parcelamento))     
else:
    print("Forma de pagamento inválida")
