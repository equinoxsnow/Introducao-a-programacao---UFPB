vi = float(input("Valor inicial:"))
jm = float(input("Juros mensal:"))
vm = float(input("Valor mensal:"))
vt = vi+(vi*jm)
valorPago = 0
juros = 0
mes = 0

while(valorPago < (vi+(vi*jm))):
    pagoNesteMes = float(input("Valor pago mensal:"))
    jurosNesteMes = pagoNesteMes*jm
    juros+= jurosNesteMes
    pagoNesteMes+= jurosNesteMes
    mes+= 1
    valorPago+= pagoNesteMes
