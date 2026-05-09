A = 0
B = 0
C = 0
jornal = 0

for contagem in range (0 , 20):
    jornal = input("Insira um jornal:").upper()

    if jornal == "A":
        A += 5
    elif jornal == "B":
        B += 5
    elif jornal == "C":
        C += 5

pa = (A * 20) / 100
pb = (B * 20) / 100 
pc = (C * 20) / 100

if pa > pb and pa > pc:
    print (pa)
elif pb > pc:
    print (pb)
    print (pc)
elif pc > pb:
    print (pc)
    print (pb)



if pb > pa and pb > pc:
    print (pb)
elif pa > pc:
    print (pa)
    print (pc)
elif pc > pa:
    print (pc)
    print (pa)



if pc > pa and pc > pb:
    print (pc)
elif pa > pb:
    print (pa)
    print (pb)
elif pb > pa:
    print (pb)
    print (pa)

