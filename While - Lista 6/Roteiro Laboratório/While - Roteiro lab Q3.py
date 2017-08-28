cont = 0
while cont < 4:
    cont+=1
    numero = int(input("Digite um número:"))
    numero2 = int(input("Digite um número:"))
    soma = (numero+numero2)
    produto = (numero*numero2)
    if (numero <= 0)  or  (numero2 <= 0):
        print("Você digitou números inválidos")
    else:
        print(soma, produto)
