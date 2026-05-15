A = []
B = []
valor = 0


for i in range (10):
    valor = int(input("Insira um valor:"))
    A.append(valor)
for j in range (9, -1 , -1):
    B.append(A[j])


print (A)
print (B)