produtos = ['manga', 'maçã', 'morango']
estoque = [100,200,50]
min_estoque = [10,20,5]

for num in range(len(produtos)):
    print(f' O produto {produtos[num]}, tem estoque {estoque[num]}, e o minimo é {min_estoque[num]}')

prod = input('Digite o nome do produto:')
qnt = int(input('Digite a quantidadede do produto:'))
minimo = int(input('Digite o minimo de estoque para o seu produto:'))
produtos.append(prod)
estoque.append(qnt)
min_estoque.append(minimo)

for num in range(len(produtos)):
    if estoque[num] <= min_estoque[num]:
        print(f'Produto {produtos[num]} com a quantidade minima')

lista = []

for num in range(len(produtos)):
    lista.append ([produtos[num], estoque[num], min_estoque[num]])
print(lista)


while True:
    busca = input('Qual produto você gostaria de remover? R:')
    if busca in produtos:
        break
    else:
        print('Produto não encontrado!')

ind = produtos.index(busca)
produtos.remove(busca)
estoque.remove(estoque[ind])
min_estoque.remove(min_estoque[ind])
print(produtos, estoque, min_estoque)







































