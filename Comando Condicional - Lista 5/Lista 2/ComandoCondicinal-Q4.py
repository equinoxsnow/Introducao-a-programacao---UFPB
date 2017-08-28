numero = int(input("Digite um número:"))
if (numero % 2) != 0 :
    res = "ímpar"
else:
    res = "não é ímpar"
if (numero % 3) == 0:
    res1 = "múltiplo de 3"
else:
    res1 = "não é múltiplo de 3"
if (102 % numero) == 0:
    res2 = "é divisor de 102"
else:
    res2 = "não é divisor de 102"
print("O número{n} é {imp},{mult} e {div}.".format(n=numero,imp=res,mult=res1,div=res2))
