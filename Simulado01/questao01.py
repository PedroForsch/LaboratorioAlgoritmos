combustivel = float(input("Insira o combustível:"))
print (f"Valor na bomba R$ {combustivel}")

revenda = combustivel * 0.83
revenda = combustivel - revenda
print (revenda)

etanol = combustivel * 0.88
etanol = combustivel - etanol
print (etanol)

icms = combustivel * 0.72
icms = combustivel - icms
print (icms)

restante = combustivel * 0.72
restante = combustivel - restante
print (restante)

despesa = revenda + etanol + icms + restante
despesa = combustivel - despesa
print (despesa)
