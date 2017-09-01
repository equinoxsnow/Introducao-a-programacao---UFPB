vendas = int(input("Total de vendas realizadas:"))
qtdadeMovel = 0
qtdadeMarca = 0
qtdadeDecor = 0
somaProd = 0
valorMedio = 0
percentual = 0
percentual2 = 0
pMarca = 0
marfim = 0
branco = 0
electrolux = 0
brastemp = 0

for c in range(vendas):
    tipoProd =str.lower(input("Digite o tipo de produto:"))

    if tipoProd == "móvel":
        cor = str.lower(input("Qual a cor do produto?"))
        qtdadeMovel+= 1
        if cor == "marfim":
            marfim+= 1
        if cor == "branco":
            branco+= 1
            
    if tipoProd == "eletrodoméstico":
        marca = input("Digite a marca do Produto:")
        if marca == "electrolux":
            electrolux+= 1
        if marca == "brastemp":
            brastemp+= 1
        else:
            "Nenhum eletrodoméstico foi vendido"
        qtdadeMarca+= 1

    if tipoProd == "decoração":
        preco = int(input("Digite o preço da decoração:"))
        qtdadeDecor+= 1
        somaProd+= preco
        valorMedio = somaProd//qtdadeDecor
        
if marfim == 0 and branco == 0:
    percentual = 0
    percentual2 = 0
    print("Percentuais: {}% marfim, {}% branco".format(percentual, percentual2))
elif marfim == branco:
    total = marfim+branco
    percentual = 100//total
    print("Percentuais: {}% marfim, {}% branco".format(percentual,percentual))
elif marfim == 0 and branco != 0:
    percentual = 0
    percentual2 = 100//branco
    print("Percentuais: {}% marfim, {}% branco".format(percentual, percentual2))
elif marfim != 0 and branco == 0:
    percentual = 100//marfim
    percentual2 = 0
    print("Percentuais: {}% marfim, {}% branco".format(percentual, percentual2))
if brastemp > electrolux:
    print("Brastemp foi mais vendida")
if electrolux > brastemp:
    print("Electrolux foi mais vendida")
if electrolux == brastemp:
    print("As duas foram vendidas igualmente")
else:
    qtdadeDecor == 0
    print("Nenhuma decoração foi vendida")
print("Preço médio: {}".format(valorMedio))
                    
        
    
        
