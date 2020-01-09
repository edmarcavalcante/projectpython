#ARQUIVOS E EXCEÇÕES

#lembre-se que o arquivo de leitura deve está guardado no mesmo diretório do programa,
# que nesse caso é o 12_arquivos_exceções.

with open("dados_pessoais.txt") as meu_dados:
	edmar = meu_dados.read()
	print (edmar)

#o programa poderia ser escrito sem o with, mas necessitaria do close para encerra-lo 
# o with é mais seguro porque o arquivo é fechado automaticamente quando n for usado.
# o close pode não ser tão seguro, pode gerar bugs no programa e o arquivo não ser fechado por alguma razão


#se o arquivo a ser lido não estiver no mesmo diretório do programa, é preciso colocar todo o caminho (path) 
# as barras não são invertidas, 
with open ("C:/Users/enged/Desktop/dados_mae.txt") as lucia:
	lucia_dados = lucia.read()
	print(lucia_dados)

print("\n")

#usando um laço for para printar linha por linha de uma arquivo texto

lucia_mae = "C:/Users/enged/Desktop/dados_mae.txt"

with open(lucia_mae) as lc:
	for line in lc:
		print(line)


#criando uma lista de linhas de um arquivo
print("\n")
edmar = "dados_pessoais.txt"

with open (edmar) as ed:
	ed_lista = ed.readlines() # esse método cria uma lista onde cada item da lista é um linha do arquivo ed

for line in ed_lista:
	print(line)

#comando para provar que ed_lista é uma lista de fato
print(type(ed_lista))

print(ed_lista[1])

#print(help(ed_lista)) - esse comando traz todos os métodos diponíveis para as listas

