# _____Pacote Pygal_____

# tipos de visualizações possíveis com o pygal: http://www.pygal.org/, clique em documentation e depois Chart types - 
# todo exemplo inclui o código fonte

#__ instalando o pacote pygal

#python -m pip instal --user pygal 

from random import randint

class Dados ():
	"""Uma classe que representa o lançamento de dados"""
	def __init__(self,num_lado = 6):
		self.num_lado = num_lado


	def lancamento(self):
		"""Devolve o valor aleatório entre 1 e o número de lado"""
		return randint(1, self.num_lado)

# simulação de 100 lançamentos de um dado com 6 lados

d = Dados() # objeto da classe criado - É uma instância

resultados = []

for x in range(1000):
	result = d.lancamento()
	resultados.append(result)


print (resultados)


# analisando as frequências dos dados
print("\n")

frequencias = []

for x in range (1, d.num_lado+1): #atenção a essa linha de comando. 
	frequenc = resultados.count(x)
	frequencias.append(frequenc)
print(frequencias)

print("\n")

#___CRIANDO UM HISTOGRAMA COM O PACOTE PYGAL PARA PLOTAR AS FREQUÊNCIAS DO LANÇAMENTO DE DADOS
import pygal

histogr = pygal.Bar() #criada a insntância de pygal.Bar()
histogr.title = "Gráfico de Frequências"
histogr.x_title = "Resultados"
histogr.y_title = "Frequência dos resultados"
histogr.x_labels = ['1','2','3','4','5','6']


histogr.add('D6', frequencias) #a função add() acrescenta uma série de valores ao gráfico
# D6 é o rótulo e frequencias é a lista de valores que aparecerão no gráfico
histogr.render_to_file('frequencia_grafico.svg') # rederização (salvando) do gráfico em um arquivo SVG

