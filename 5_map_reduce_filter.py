# Funções MAP, REDUCE e FILTER

# Podemos usar as funções map(), reduce() e filter() para aplicar uma determinada função a uma sequência de dados


# FUNÇÃO MAP

# Atenção: as funções MAP, REDUCE e FILTER são semelhantes, todas elas recebem 2 argumentos: uma função e uma sequência
# EX: MAP (função, sequência), REDUCE (funação, sequência), FILTER (função, sequência)

# Primeiro criou-se uma lista com valores de temperatura em graus celsius
celsius = [10, 15, 20, 30, 35, 40, 45, 50]

# Agora criou-se uma função simples que transforma graus celsius em fahrenheit 
def fahrenheit (c):
	return ((float(c)*1.8) + 32)

# Aqui é a aplicação da função MAP. 
# Ela permite que a função fahrenheit seja aplicada automativamente a cada item da lista (celsius)
print(list(map(fahrenheit,celsius)))


print('\n')


fahrenheit = [10, 15, 20, 25, 30]

def celsius (fa):
	return((float(fa)-32)/1.8)

print(list(map(celsius,fahrenheit)))
print('\n')

# Outra utilização da função map 

lista_1 = [2,3,4,5,6]
lista_2 = [10,12,13,14,15]

print(list(map(lambda x,y: x + y, lista_1,lista_2))) 
print('\n')
#o map somou cada elemneto das respectivas lista e criou um lista com o resultado.


#FUNÇÃO REDUCE

from functools import reduce # é preciso importar a função REDUCE

lista_1 = [2,3,4,5,6]
lista_2 = [10,12,13,14,15]
lista_3 = lista_1 + lista_2

def soma_total(a,b):
	soma= a+b
	return soma

print(reduce(soma_total,lista_3))
print('\n')

print(reduce(lambda a,b: a+b,lista_3))

print('\n\n')

# Utilização da função FILTER

# Primeiro vou criar uma função para saber se um número é par ou não

def num_par (n):
	if n % 2 == 0:
		return True
	else:
		return False

# agora eu criou um lista onde quero aplicar a função FILTER

lista_filter = []
# criei uma lista vazia e depois inclui 30 números nela.
count = 0
for x in range(0,30):
	count =+ x
	lista_filter.append(count)
print(lista_filter)
print("\n")

#como já foi dito, a função Filter recebe (função, sequência)
print(list(filter(num_par, lista_filter)))

# função LAMBDA também segue esse padrão: recebe um argumento, uma função e uma sequência
lista_lambda = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, lista_lambda)))