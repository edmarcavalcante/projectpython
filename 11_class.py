# ESTUDO DE CLASSES

# por convenção, a criação de uma classe deve ser feito com a inicial maíscula

# classe>método>atributos>instâncias
class Carro ():
	#abaixo foi criado a método construtor, que não passa de uma função: def __init__
	def __init__(self, modelo, ano, preco): #entre parênteses estão os parâmetros.
		#abaixo foram criado os atributos
		self.modelo=modelo
		self.ano=ano
		self.preco=preco
# Métodos são funções, que recebem como parâmetro atributos do objeto criado
	def imprimecarro (self):
		print("O modelo do carro é {}, seu ano de fabricação é {} e custa {}".format(self.modelo,self.ano,self.preco))

#aqui foram criadas as instâncias 

carro1 = Carro("Corsa",1990,10000) #observe que não foi preciso chamar o parâmetro self
carro2 = Carro("Fox", 2005,21000)
carro3 = Carro("monza", 2000, 15000)

print(carro1.imprimecarro()) #__esse comando chama a instância carro1 
                             # juntamnete com o método impremecarro contido na class Carro

print(carro2.imprimecarro())
print(carro3.imprimecarro())

print(carro1.modelo)
print(carro2.preco)
print(carro3.ano)

# Criando um objeto a partir da classe Carro

carro4 = Carro("hb20", 2015,29000)
print(carro4.imprimecarro())

#importante conhecer alguns atributos que permitem trabalhar com classes: hasattr, setattr, getattr, delattr

#python perguntando se a instância carro1 tem o atributo "modelo". A resposta é True ou False
print("\n")
print(hasattr(carro1,"modelo"))
print("\n")

#python perguntando se a instância carro2 tem o atributo "preço"
print("\n")
print(hasattr(carro2, "preco"))

#python está alterando o ano da instância carro3. Antes era 2000, agora passa a ser 2010
setattr(carro3, "ano", 2010)

print(getattr(carro3,"ano"))

print(carro3.imprimecarro())

#CRIANDO UMA HERANÇA DA CLASSE PRINCIPAL - SUBCLASSE

#criando a classe principal animal

class Animal():
	def __init__(self, idade, cumprimento, sexo):
		self.idade=idade
		self.cumprimento=cumprimento
		self.sexo=sexo

	def caminhar():
		print("Animal caminhando")

class Ave (Animal):
	def 




 		 
		