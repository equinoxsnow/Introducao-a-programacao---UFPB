distancia = float(input("Quantos quiloômetros deseja viajar?"))
cobranca1 = 0.50
cobranca2 = 0.45
if distancia <= 200:
    print(distancia*cobranca1)
elif distancia > 200:
    print(distancia*cobranca2)
