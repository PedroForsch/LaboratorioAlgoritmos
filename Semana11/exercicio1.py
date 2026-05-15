elementos = []
valor = 0
somatodos = 0
soma30 = 0
numero = 0

for i in range (8):
    valor = int(input("Insira um valor:"))
    elementos.append(valor) 
    somatodos += valor

    if valor > 30:
        numero += 1
        soma30 += valor


print (f"A soma de todos os valores é {somatodos}")
print (f"A soma dos números > 30 é {soma30}")
print (f"Existem {numero} maiores que 30")
