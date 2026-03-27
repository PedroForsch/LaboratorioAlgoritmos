valor_compra = float(input("Valor da compra:"))
print (f"1 - A vista (25% de desconto)")
print (f"2 - Em 2x (16% de desconto)")
print (f"3 - Em 3x (4% de desconto)")
print (f"4 - Em 4x (8% de juros)")
opcao = int(input("Digite a opção:"))

if opcao == 1:
    valor_final = valor_compra * 0.75
    print ("Valor com desconto:", valor_final )
elif opcao == 2:
    valor_final = valor_compra * 0.84
    parcela = valor_final / 2
    print ("Valor parcela:", parcela)
    print ("Valor com desconto:", valor_final )
elif opcao == 3:
    valor_final = valor_compra * 0.96
    parcela = valor_final / 2
    print ("Valor parcela:", parcela)
    print ("Valor com desconto:", valor_final )
elif opcao == 4:
    valor_final = valor_compra * 1.08
    parcela = valor_final / 4
    print ("Valor parcela:", parcela)
    print ("Valor com desconto:", valor_final )
else:
    print ("Opção inválida!")


