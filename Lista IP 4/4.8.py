a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
operação =(input("Qual operação deseja realizar?"))
soma = ("+")
subtração = ("-")
multiplicação = ("*")
divisão = ("/")
if operação == "soma":
    print(a+b)
elif operação == "subtração":
    print(a-b)
elif operação == "multiplicação":
    print(a*b)
elif operação == "divisão":
    print(a/b)
