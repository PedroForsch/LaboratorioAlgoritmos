#TIPO 1 - SEM PARAMETROS E SEM RETORNO
def ola():
    nome = input("Digite seu nome:")
    print("Olá, você está dentro da função")

#TIPO 2 - COM PARAMETROS E SEM RETORNO

def olanovo(nome):
    print(f"Olá,{nome} você está dentro da nova função")

#TIPO 3 - COM PARAMETRO E COM RETORNO
def olanov(nome):
    nome = "Marcos"
    return nome


def main():
    #ola()
    n = input("Digite seu nome novamente:")
    #olanovo(n)
    n = olanov(n)
    print (f"Novo nome {n}")

main()