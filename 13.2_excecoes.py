# continuação de arquivos e exceções

#_____USO DO BLOCO TRY-EXCEPT_____#

# exemplo básico. Em python, assim como na matemática, não se pode dividir 
# um número por zero, pois não há resultado. Veremos que o erro apresentado 
# pelo python quando tentamos fazer essa operação

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe outro número: "))

print("Vamos dividí-los")
print('\n')

divisao = numero1/numero2

print(divisao) 
print('\n')

# essa operação vai trazer erro se o segundo número for zero

#forma de tratar esse erro - excecão

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe outro número: "))
print('\n')
print("Vamos dividí-los")
print('\n')

try:
	divisao = int(numero1)/int(numero2)

except ZeroDivisionError: #é preciso colocar o nome do erro após o comando except
# cada tipo de erro tem um nome diferente	
	print("Não se pode dividr um número por zero")

else:
	print(divisao)


# programa para ler arquivos aplicado o conceito de errro-exceções

arquivos_lista = ["arquivo_novo.txt", "dados_pessoais.txt", "livros_lidos_2019.txt", "casa.txt"]

#vou criar uma função para fazer esse trabalho de leitura de arquivos

def ler_arquivo (nome_arquivo):
	
	try:
		with open (nome_arquivo) as ler:
			leitura = ler.read()
	except FileNotFoundError:
		print("Desculpe, mas esse arquivo não está no diretório")

	else:
		print(leitura)


print(ler_arquivo("arquivo_novo.txt"))
print('\n')
print(ler_arquivo("dados_pessoais.txt"))
print('\n')
print(ler_arquivo("casa.txt")) # nesse caso, a função vai apresentar a mensagem de except
# pois o arquivo casa.txt não está no diretório.

# AGORA APLICAR A FUNÇÃO EM UM LOOP FOR
arquivos_lista = ["arquivo_novo.txt", "dados_pessoais.txt", "livros_lidos_2019.txt", "casa.txt"]
for arq in arquivos_lista:
	print(ler_arquivo(arq))
	print('\n')