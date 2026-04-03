forca1 = float(input("Digite o valor da primeira força:"))

forca2 = float(input("Digite o valor da segunda força:"))

forca3 = float(input("Digite o valor da terceira força:"))

if forca1 + forca2 > forca3 or forca1 + forca3 > forca2 or forca2 + forca3 > forca1:
    if forca1 == forca2 == forca3:
        print("Simétrico")

    elif forca1 == forca2 or forca2 == forca3 or forca1 == forca3:
        print("Parcialmente Simétrico")

    elif forca1 != forca2 != forca3:
        print("Assimétrico")

else:
    print("Não há equilíbrio")