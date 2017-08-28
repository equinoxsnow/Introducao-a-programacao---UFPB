gasolina = 2.53
etanol = 2.09
diesel = 1.92
tipoCombustivel = str.lower(input("Qual o tipo de combustível que deseja abastecer?"))
valor = float(input("Quanto reais pretende gastar?"))
if (tipoCombustivel == "gasolina"):
    litros = valor / gasolina
    print("Você abasteceu %.2f"%litros, "e não ganhou uma troca de óleo")    
elif (tipoCombustivel == "etanol"):
    litros = valor / etanol
    if (litros >= 30):
       print("Você abasteceu %.2f"%litros, "e ganhou uma troca de óleo")     
    else:
        print("Você abasteceu %.2f"%litros, "e não ganhou uma troca de óleo")    
else:
    litros = valor / diesel
    print("Você abasteceu %.2f"%litros, "e não ganhou uma troca de óleo")    
    
    
        
    

