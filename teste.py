#teste
import csv

arq = "sitka_weather_2018_simple.csv"

with open(arq) as f:
	ler = csv.reader(f)
	colum = next(ler)
	print(colum)

	for indice, coluna in enumerate(colum):
		print (indice, coluna)


	data = []

	for x in ler:
		date1=x[2]
		data.append(date1)
print(data)