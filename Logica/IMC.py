print ("Olá, mundo!")
print ("Vamos calcular o seu IMC!")

x = float(input("Me fale quão gordo você é: "))
y = float(input("Me fale quão alto você é: "))

z = x/(y*y)

if (z <= 18.5):
    print("Magreza")
elif (z > 18.5 and z < 24.9):
    print("Normal")
elif (z > 25 and z < 29.9):
    print("Sobrepeso")
elif (z > 30 and z < 34.9):
    print("Obesidade grau 1")
elif (z > 35 and z < 39.9):
    print("Obesidade grau 2")
else:
    print ("Seu IMC é de:")