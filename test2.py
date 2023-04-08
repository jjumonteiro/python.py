n = int (input("Informe a tabuada que deseja treinar:"))
acertos = 0
erros = 0
for nTab in range(1, 11):
    print("\n", n, "x", nTab, "=" )
    resp = int (input("R:"))
    if resp == nTab*n:
        print ("Parabéns, você acertou!")
        acertos += 1
    else:
        print ("Sua resposta esta errada, o resultado é:" )
        erros += 1
print("\nTotal de acertos:", acertos)
print("Total de erros", erros)