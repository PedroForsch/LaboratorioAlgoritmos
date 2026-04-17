oliveira = int(input("Insira a idade da oliveira em anos:"))
altura = oliveira * 30
altura = altura / 100
print (altura, "metros")
if altura >= 5:
    print ("Oliveira Adulta")
elif altura < 5:
    print ("Oliveira em crescimento")