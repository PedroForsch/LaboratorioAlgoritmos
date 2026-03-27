valor = 0
p1 = input("Você esteve no local do crime?").lower()
if p1 == "sim":
    valor += 1

p2 = input("Você conhece a vítima?").lower()
if p2 == "sim":
    valor += 1

p3 = input("Você já teve algum desentendimento com a vítima?").lower()
if p3 == "sim":
    valor += 1

p4 = input ("Você estava próximo ao local na hora do ocorrido?").lower()
if p4 == "sim":
    valor += 1

p5 = input ("Você tem algo que comprove sua inocência?").lower()
if p5 == "sim":
    valor -= 1
else:
    valor += 1

if valor >= 3:
    print ("Pessoa suspeita")
else:
    print ("Pessoa não considerada suspeita.")
