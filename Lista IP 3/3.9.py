dias= int(input("Insira os dias:"))
horas= int(input("Insira as horas:"))
minutos= int(input("Insira os minutos"))
segundos= int(input("Insira os segundos"))
diasseg= (dias*84600)
horasseg= (horas*3600)
minutosseg= (minutos/60)
seg= segundos
print (diasseg+horasseg+minutosseg+seg)
