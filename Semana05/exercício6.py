maca = float(input("Quantos KGs de maçã você quer comprar?"))
morango = float(input("Quantos KGs de morango você quer comprar?"))

peso = maca + morango

print (f"Você comprou {maca} KGs de maçã")
print (f"Você comprou {morango} KGs de morango")

if maca <= 5:
        valormaca = maca * 1.80

elif maca > 5:
       valormaca = maca * 1.50

if morango <= 5:    
    valormorango = morango * 2.50
elif morango > 5:
        valormorango = morango * 2.20

valortotal = valormaca + valormorango

if valortotal > 25 or peso > 8:
        valortotal2 = valortotal * 0.90

print (f"O valor sem desconto é {valortotal}")  
print (f"O valor com desconto é {valortotal2}")     
        