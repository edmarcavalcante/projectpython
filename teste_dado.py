#teste lançamento de dado

from random import randint

class Meu_dado():
	def __init__(self,lados = 6):
		self.lados=lados

	def lance(self):
		return randint(1,self.lados)

dado1 = Meu_dado(6)

lista = []

for x in range(1,100):
	res = dado1.lance()
	lista.append(res)

print (lista)


dado2 = Meu_dado(10)


lista2 = []
frequencia = []

for x in range(1,100):
	result1 = dado1.lance()
	lista2.append(result1)
	result2 = dado2.lance()
	lista2.append(result2)
	lista3 = lista+lista2
	#soma = result1 + result2
print("Minha conjunto de dados é: " + str(lista3))
	
print("\n")
print(len(lista))

print("\n")
print(len(lista2))
	#for n in range (1,self.lados+1):
		#freque = lista2.count(n)
		#frequencia.append(freque)
#print (frequencia)
print("\n")
for n in range (1,dado2.lados+1): #atenção a essa linha de comando. dados2.lados
	freq = lista3.count(n)
	frequencia.append(freq)
print(frequencia)
