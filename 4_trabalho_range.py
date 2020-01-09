#criando uma lista COMPREHENSIONS. É uma fora de escrever um código mais limpo, sem muitas linhas

lista_potencia = []

for x in range(1,10):
	raiz = x**2
	lista_potencia.append(raiz)
print(lista_potencia)
print('\n')

# utilizando o método LIST COMPREHENSIONS a lista fica mais enxuta, veja:

lista_cubo = [x**3 for x in range(1,10) if x%2 == 0]
print(lista_cubo)
print('\n')

lista_cubo = [x**3 for x in range(1,10)]
print(lista_cubo)
#primeiro você coloca a fórmula, em seguida você escreve o loop for range