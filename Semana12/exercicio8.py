def conversao (int1 , int2):
    if int1 > 12:
        int1 = int1 - 12
    return int1 , int2

def saida (conversao1 , conversao2):
    if conversao1 > 12:
        print (f"São {conversao1}:{conversao2} PM")
    else:
         print (f"São {conversao1}:{conversao2} AM")
    

def main():
    int1 = int(input("Insira o primeiro valor inteiro:"))
    int2 = int(input("Insira o segundo valor inteiro:"))
    if int1 >= 0 and int1 <= 23 and int2 >= 0 and int2 <= 59:
        conversao1 , conversao2 = conversao(int1 , int2)
        saida(conversao1 , conversao2)
    else:
        print("Inválido!!")
main()


