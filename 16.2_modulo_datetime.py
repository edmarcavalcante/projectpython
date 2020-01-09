# Módumo datetime
import csv
from matplotlib import pyplot as plt
from datetime import datetime

arq = "sitka_weather_2018_simple.csv" #salvei o caminho do arquivo que será trabalhado na variável 'arq'

with open(arq) as f: #abrimos o arquivo
	reader = csv.reader(f) #
	head_reader = next(reader) #o módulo csv tem a função next que devolve a primeira linha do arquivo csv
	print(head_reader)

# O comando a seguir é uma forma mais interessante de conhecer os dados, de modo que ele traz
# a localização das colunas (índice) e seus respectivos valores. Isso é relevante para conhecer as colunas da tabela 
	
	for indice, coluna in enumerate(head_reader): # a função enumerate traz os indices e valores
		print(indice, coluna) # atenção - esse comando deve estar indentado, pois só funciona com o
		# modo de leitura ativo (reader)

	tmax, datas = [], []  #criei duas listas vazias que irão receber os dados das temperaturas máximas e datas

	tmin = [] #criei a lista que receberá as temperaturas mínimas. Posteriormente será plotada no gráfico também

	for x in reader: # o loop deve ser feito em reader, pois é a variável que contém os registros csv
		max = int(x[5]) #lembrando as strings em números inteiros, de modo que posso ser trabalhado pela matplotlib
		tmax.append(max)
 
 		#aqui foi utilizado o método strptime() do módulo datetime.
 		# esse método recebe 2 argumentos, o primeiro é a informação de data que iremos trabalhar,
 		# o segundo informa ao python como a data será formatada 	
		d = datetime.strptime(x[2],"%Y-%m-%d") # preciso estudar sobre o módulo datetime
		datas.append(d)

		min = int(x[6]) #extraindo os dados de temp mínima da tabela e alimentado a lista que foi criada
		tmin.append(min)	



print (tmin)
print('\n')
print(datas)

plt.plot(datas,tmax)
plt.plot(datas,tmin)
plt.title("Temperaturas Máximas e Mínimas 2018")
plt.show()