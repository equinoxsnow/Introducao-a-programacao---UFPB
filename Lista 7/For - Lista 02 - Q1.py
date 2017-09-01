quantItem = int(input("Quantidade de peças:"))
maiorValor = 0
vali = 0
valorFinal = 0
precoMaior = 0
maisVali = 0
anoMaisVali = 0


for c in range(quantItem):
    tipoItem = input("Peça:")
    valorItem = float(input("Valor do Item:"))
    anoItem = int(input("Ano do Item:"))
    if (anoItem <= 1827):
        vali+= 1
    if valorItem > precoMaior:
        precoMaior = valorItem
        maisVali = tipoItem
        anoMaisVali = anoItem
    valorFinal+= valorItem
valorMedio = valorFinal / quantItem
    
print("%d itens foram produzidos antes de 1827"%vali)
print("Valor médio dos itens: %s"%valorMedio)
print("Objeto mais valioso é {},{}".format(maisVali,anoMaisVali))
