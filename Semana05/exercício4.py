
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) /2

print (f"Suas notas foram {nota1} e {nota2}")
print (f"Sua média é {media}")

if media >= 9 and media <= 10:
      print ("Conceito A: Aprovado")
elif media >= 7.5 and media < 9:
      print ("Conceito B: Aprovado")
elif media >= 6 and media < 7.5:
      print ("Conceito C: Aprovado")

elif media >= 4 and media < 6:
      print ("Conceito D: Reprovado")
elif media < 4:
    print ("Conceito E: Reprovado")
