#LAÇOS WHILE
# criando uma string múltipla
message = "we would like of the know your name. Be would better for startig the conversation."
message += "\nWhat your name, please? "
nome = input(message)
print("Welcome, "+ nome.title()+"!")

# atenção: a função input por natureza recebe um comando em string, e devolve com a mesma estrutura (string)
# se quiser que a entrada da função input seja um número, é necessário que você coloque int(input())

# o laço FOR é != de WHILE. O laço For pega uma coleção de dado e aplica uma função em cada item da coleção; 
# já o laço While aplica a função enquanto determinanda condição for verdadeira.

from time import sleep
print("Vamos começar a estudar laço while!")
print(sleep(2))
current_number = 1
while current_number <= 10:
	if current_number >= 5:
		print(current_number)
	current_number += 1
	
# aqui eu quis apenas os números entre 5 e 10

# exercício: escrever um laço que peça ao usuário para fornecer uma série de ingredientes para uma pizza
#até que o valor 'quit' seja fornecido. À medida que cada ingrediente é especificado, apresente uma messagem
# que você acrescentará esse ingrediente à pizza.

print ("Seja bem vindo a Pizzaria do Ed!")
print("\nAqui você escolhe os ingredientes")
print(sleep(2))
print("Vamos começar!, caso não queira incluir mais ingredinetes é só digitar 'sair'. ")
chamada = "Me fale qual ingrediente posso incluir em sua pizza: "
print(sleep(1))
lista_ingrediente = []
msg = " "
while msg != "sair": #__ esse laço é semelhante ai - while true: ... break
	msg = input(chamada)
	lista_ingrediente.append(msg)
	print(msg)
	if len(lista_ingrediente) == 4:
		print("chegou ao limite de ingredientes, que são 4")
		print(lista_ingrediente)
		for x in lista_ingrediente:
			print(x)
		break

print("\nVAMOS COMEÇAR NOVAMENTE?")

# Usando a estrutura flag

suco = "WELCOME THE MY NEW JOICE' SHOP"
suco += "\nCHOOSE WHAT FLAVOR OF THE JOICE YOU'LL WANT: if you don't want more, type 'exit'"

flavor = " "
variavel_flag = True # um exemplo do laço while true:... brek(False)
# a variável "variavel_flag" é o comando flag 
while variavel_flag:
	flavor = input(suco)
	print("\n" + flavor.upper() + "\n")

	if flavor == "exit":
		variavel_flag = False



