pedidos = int(input("Digite a quantidade de Pedidos!"))
valorTotal = 0
qtdadeSeco = 0
v = list(range(pedidos))

for c in range(pedidos):
    tipoCobranca = str.lower(input("Qual o tipo de cobrança?"))
    
    if tipoCobranca == 'peça':
        quantidadePecas = int(input("Quantidade de peças?"))
        valorPeca = quantidadePecas*7
        lavagemSeco = str.lower(input("Lavagem a seco?"))
        if lavagemSeco == 'sim':
            valorPecaSeco = (valorPeca + 3.5)
            valorTotal+= valorPecaSeco
            qtdadeSeco+= 1
        else:
            valorPecaSeco = valorPeca
            valorTotal+= valorPecaSeco
        
    elif tipoCobranca == 'peso':
        quantidadeQuilos = int(input("Digite a quantidade de quilos!"))
        valorPeca = quantidadeQuilos*5
        lavagemSeco = str.lower(input("Lavagem a seco?"))
        if lavagemSeco == 'sim':
            valorPecaSeco = (valorPeca + 3.5)
            valorTotal+= ValorPecaSeco
            qtdadeSeco+= 1
        else:
            valorPecaSeco = valorPeca
            valorTotal+= valorPecaSeco
    v[c] = valorPecaSeco
for c in range(pedidos):
    print("Valor do pedido: {} ".format(v[c]))
print ("Total arrecadado: {} \nQuantidade de lavagens a Seco: {}".format(valorTotal,qtdadeSeco))

        
        
    
