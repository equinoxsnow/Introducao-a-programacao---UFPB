cont = 0
while cont < 4:
    cont+=1
    numero = int(input("Digite um n�mero:"))
    numero2 = int(input("Digite um n�mero:"))
    soma = (numero+numero2)
    produto = (numero*numero2)
    if (numero <= 0)  or  (numero2 <= 0):
        print("Voc� digitou n�meros inv�lidos")
    else:
        print(soma, produto)
