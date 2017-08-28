velocidade = float(input("Velocidade do usuário:"))#Em km/h
if velocidade > 80:
    ultrapassagem = velocidade - 80
    multa = ultrapassagem * 5
    print ("Você ultrapassou 80km/h, sua multa é de %sR$" %(multa))
else:
        print ("Você não ultrapassou os 80km/h, que ótimo")
    
    
