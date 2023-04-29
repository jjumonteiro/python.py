produtos: {"Mouse": 98.75  "Teclado": 125.65 "Monitor": 134.78 "Gabinete": 170.00 "HD externo": 510.50 "Headset": 125.45}

while true:
    produto = input("Informe o produto ao pesquisar o preço ou fim para sair:")
    if produto == "fim":
        break 
    if produto in produtos:
        print(f"Produto{Produto} custa {Produtos[produto]}.")
    else:
         print(f"Produto{Produto} não encantardo. ")
