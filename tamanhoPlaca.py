MaxX= int(input("Informe a largura de sua placa:"))
MaxY = int(input("Informe a altura de sua placa:"))
M = int(input("Informe o numero de sua placa:"))
for M in range(M):
    X = int(input("Informe a largura da placa:"))
    Y = int(input("Informe o comprimento da placa:"))
    if X <= MaxX and Y <= MaxY:
        print("Dá para construir.")
    else:
        if X <= MaxX and Y <= MaxX:
            print("Dá para construir.")
        else:
            print("Não dá para construir.")