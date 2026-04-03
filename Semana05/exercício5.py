
p1 = input("Você treinou regularmente nas últimas semanas?").upper()
p2 = input("Participou de treinos longos (acima de 10 km)?").upper()
p3 = input("Seguiu uma dieta especial para a corrida?").upper()
p4 = input("Já competiu em provas oficiais neste ano?").upper()
p5 = input("Conta com acompanhamento de treinador ou equipe?").upper()

valor = 0

if p1 == "SIM":
    valor += 1
if p2 == "SIM":
    valor += 1
if p3 == "SIM":
    valor += 1
if p4 == "SIM":
    valor += 1
if p5 == "SIM":
    valor += 1

if valor == 2: 
    print ("Você está classificado como Participante Casual(ainda precisa de mais treino)")
if valor == 3 or valor == 4:
    print ("Você é classificado como Atleta Competitivo (tem boas chances de se destacar).")
if valor == 5:
    print ("Você é classificado como Atleta de Elite (pronto para o pódio!).")
if valor < 2:
    print("Você é classificado como Não Preparado (talvez seja melhor assistir da arquibancada este ano).")