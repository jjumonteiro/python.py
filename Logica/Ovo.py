print ("Olá, mundo!")

x = str(input("Por favor, me informe o tamanho desejado: (Pequeno, Médio ou Grande)"))
y = str(input("Agora me informe o sabor desejado: (Chocolate preto, Chocolate branco e Chocolate ao leite)"))
z1 = str(input("Agora o sabor do recheio: (Chocolate preto ou Chocolate branco)"))
z2 = str(input("Gostaria de outro recheio? Se sim, qual? (Não) (Sim, Chocolate preto ou Sim, Chocolate branco)"))
a = str(input("Você também ter a opção de adicionais, gostaria de adicionar algum? Se sim, qual? (Não) (Sim, KitKat ou Sim, MM's)"))
b = str(input("O produto será presente? (Sim ou Não)"))
c = str(input("Será para entrega? (Sim ou Não)"))
p = str(input("Como gostaria de realizar o pagamento? (Cartão de crédito, Dinheiro/Pix)"))
q = str(input("Qual será a quantidade de OVOS DO MARCELO?"))
v = 0
v2 = v + 0
v3 = v2 + 0
v4 = v3 + 0
v5 = v4 + 0
v6 = v5 + 0
v7 = v6 + 0
v8 = v7 + 0 
v9 = v8 + 0
vf = v9

if (x == "Pequeno"):
    v = (v + 7.8)
elif (x == "Médio"):
    v = (v + 12.9)
elif (x == "Grande"):
    v = (v + 23.95)
elif (y == "Chocolate preto"):
    v2 = (v2 + 9.67)
elif (y == "Chocolate branco"):
    v2 = (v2 + 4.5)
elif (y == "Chocolate ao leite"):
    v2 = (v2 + 9.32)
elif (z1 == "Chocolate preto"):
    v3 = (v3 + 4.83)
elif (z1 == "Chocolate branco"):
    v3 = (v3 + 2.25)
elif (z2 == "Não"):
    v4 = (v4 + 0)
elif (z2 == "Sim, Chocolate preto"):
    v4 = (v4 + (4.83/2))
elif (z2 == "Sim, Chocolate branco"):
    v4 = (v4 + (2.25/2))
elif (a == "Sim, KitKat"):
    v5 = (v5 + 4.67)
elif (a == "Sim, MM's"):
    v5 = (v5 + 5.43)
elif (b == "Sim"):
    v6 = (v6 + 2.5)
elif (b == "Não"):
    v6 = (v6 + 0)
elif (c == "Sim"):
    v7 = (v7 + 5)
elif (c == "Não"):
    v7 = (v7 + 0)
elif (p == "Cartão de crédito"):
    v8 = (v8 + 3,30)
elif (p == "Dinheiro/Pix"):
    v8 = (v8 * 0.1)
elif (q <= 0):
    v9 = (v8 * q) 

print(vf)