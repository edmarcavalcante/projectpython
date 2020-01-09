# módulo json

# de modo geral, o módulo json trabalha com duas funções: json.dump() e json.load()

# A função json.dump() é utilizada para salvar o arquivo no formato json
# A função json.load() é utilizada para imprimir o arquivo que fora salvo no formato json
# Antes de começar, é priciso importar o módulo json
# Atenção, a função json.dump() aceita 2 argumentos: primeiro i- o dado a ser armazenado, e ii- o objeto arquivo que 
#pode ser usado para armazenar 

import json

yourname = input("What is your name? ")
listaname = []
filename = 'yourname.json'#variável onde será armazenado o nome em formato json

with open (filename, 'w') as file:#abrindo o arquivo filename para escrita
	json.dump(yourname,file)
	listaname.append(yourname) #aqui estou improvizando para salvar o nome na lista
	print("Bem vindo, "+yourname+"!")

print(listaname)
print('\n')

# Agora o arquivo será lido por meio da função json.load()

with open (filename) as file:
	name1 = json.load(file)#usei a função json.load() para carregar as informações armazenadas em yourname.json
						   # e as guardei na variável name1	
	print('Olá, '+name1+'!')


