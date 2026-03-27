nome = input("Qual seu nome?")
valor = float(input("Qual o valor da compra?"))
pagamento = int(input("Qual a forma de pagamento?(1 para dinheiro)(2 para cartão)"))

print ("Seu nome é", nome)
print ("O valor inicial da sua compra é", valor)

if valor > 200:
  if pagamento == 1:
   valorfinal1= valor * 0.85
   print ("A sua compra ficou", valorfinal1, "Reais")
  else: 
    valorfinal2 = valor * 0.95
    print ("A sua compra ficou", valorfinal2, "Reais")

if valor < 200:
 if pagamento == 1:
  valorfinal3 = valor * 0.90
  print ("A sua compra ficou", valorfinal3, "Reais")
 else:
   print ("Sem desconto")