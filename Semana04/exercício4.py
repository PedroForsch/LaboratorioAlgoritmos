
inscricao = float(input("Qual o valor da inscrição?"))

pagamento = int(input("Qual a forma de pagamento? A vista(1), em 2x (2)," \
"em 3x (3)"))

if pagamento == 1:
    valorfinal = inscricao
    print (f"O valor da inscrição é {inscricao:.2f}")
    print (f"A forma de pagamento escolhida é a vista")
elif pagamento == 2:
    valorfinal = inscricao / 2
    print (f"O valor da inscrição é {inscricao:.2f}")
    print (f"A forma de pagamento escolhida é a vista")
    print (f"O valor da parcela é {valorfinal:.2f}")
elif pagamento == 3:
    valorfinal = inscricao / 3
    print (f"O valor da inscrição é {inscricao:.2f}")
    print (f"A forma de pagamento escolhida é a vista")
    print (f"O valor da parcela é {valorfinal:.2f}")
else:
    print ("Inválido!")
    