# continuação de arquivos e exceções

with open("livros_lidos_2019.txt") as lv:
	l = lv.read()#método para ler o arquivo texto
	print(l)

print('\n')


#with open("livros_lidos_2019.txt") as lv:
	#l = lv.write("ler é enriquece a alma") - esse comando deve ser
	# utilizado com cuidado, pois ele sobrescreve o documento, apagando o que tinha antes.

print('\n')

#tentativa de criar um arquivo novo

arquivo = open("arquivo_novo.txt", "w")
arquivo.close()

#foi criado um arquivo novo chamado "arquivo_novo.txt"
#vamos trabalhar com ele

with open("arquivo_novo.txt", "w") as newdoc:
	an=newdoc.write("Essa é a primeira frase do arquivo")

print(an)#mandei executar, mas não vai aparecer o conteúdo do arquivo,
#pois ele está fechado.

#forma de acessar o conteúdo do arquivo
with open('arquivo_novo.txt','r') as ler:
	print(ler.read())

#acrescentar texto sem sobrescrever o que já foi escrito
# concatenando dados em arquivo
with open ('arquivo_novo.txt', 'a') as add:
	add.write('\nEu estou acrescentando linhas no meu arquivo')
	add.write('\nEssa é a linha final')

#Exercício: digitar o título de um livro e ver se ele está no 
#arquivo 'livros_lidos_2019'

with open('livros_lidos_2019.txt') as lv2019:
	lv = lv2019.readlines()

string_unica_livro = ''

for i in lv:
	string_unica_livro += i.rstrip() #esse método remove o caractere de quebra de linha

print(string_unica_livro)

livro1 = input(str('Escolha o título de um livro: '))

if livro1.title() in string_unica_livro:
	print('Eu li esse livro em 2019')
else:
	print('Eu preciso ler esse livro ainda esse ano')