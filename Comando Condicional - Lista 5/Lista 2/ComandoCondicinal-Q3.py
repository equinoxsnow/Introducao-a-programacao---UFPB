a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))
if a > b and a > c:
    res = "O primeiro é maior"
elif b > a and b > c:
    res = "O segundo é maior"
else:
    res = "O terceiro é maior"
print(res)
