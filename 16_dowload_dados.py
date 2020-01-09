#____DOWNLOAD DE DADOS____

#_primeiro devemos importar o módulo que trata de arquivos formato CSV

import csv

arq = "sitka_weather_2018_simple.csv" #salvei o caminho do arquivo que será trabalhado na variável 'arq'

with open(arq) as f: #abrimos o arquivo
	reader = csv.reader(f) #
	head_reader = next(reader) #o módulo csv tem a função next que devolve a primeira linha do arquivo csv
	print(head_reader)

# O comando a seguir é uma forma mais interessante de conhecer os dados, de modo que ele traz
# a localização das colunas (índice) e seus respectivos valores 
	
	for indice, coluna in enumerate(head_reader): # a função enumerate traz os indices e valores
		print(indice, coluna)

	tmax = []  #criei uma lista vazia que irá receber os dados das temperaturas máximas

	for x in reader: # o loop deve ser feito em reader, pois é a variável que contém os registros csv
		max = int(x[5]) #lembrando as strings em números inteiros, de modo que posso ser trabalhado pela matplotlib
		tmax.append(max)
 
print (tmax)

