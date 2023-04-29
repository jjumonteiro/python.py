A = int(input("Informe um número:")) 
B =  int(input("Informe outro número:")) 

if (A == 0 or B == 0):
     print("Impossível dividir seu número por zero!") 
else:
    if (A%B == 0):
        print ("O primeiro número é divisível pelo segundo número")

    else:
        print("O primeiro número não é divisivel pelo segundo número")