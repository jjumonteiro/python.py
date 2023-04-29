         
filmes = {}

filmes["Barbie em Vida de Sereia"] = {"vilão": "Eris", "ano": 2010}
filmes["Enrolados"] = {"vilão": "Vladimir", "ano": 2010 }
filmes["Meu malvado favorito"] = {"vilão": "Vector", "ano": 2010 }
filmes["Megamente"] = {"vilão": "Titan", "ano": 2010 }
filmes["diario de um Banana"] = {"vilão": "Greg Heffley", "ano": 2010 }

print (filmes)

while True:
  filmeNovo = input("Digite o nome do filme (digite 0 para sair): ")
  if filmeNovo == '0':
    break
  vilaoNovo = input("Digite o nome do Vilão: ")
  anoNovo = input("Digite o ano do filme: ")
  filmes[filmeNovo]={'vilão': vilaoNovo, 'ano': anoNovo}
print(filmes)
pesquisa = input('digite o filme procurado: ')
if pesquisa in filmes:
  print(filmes[pesquisa])