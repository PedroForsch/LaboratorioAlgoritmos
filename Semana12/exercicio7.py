def somaImposto(custo , taxa):
    if taxa > 0:
        taxa = (taxa / 100) + 1
    print (f"A taxa é {taxa}")
    valor_alterado = custo * taxa
    return valor_alterado

def main():
    custo = float(input("Insira o custo:"))
    taxa = int(input("Insira uma taxa:"))
    valor_alterado = somaImposto(custo , taxa)
    print (f"O valor alterado é R${valor_alterado:.2f}")

main()