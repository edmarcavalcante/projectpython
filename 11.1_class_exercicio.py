# prática dos exercícios do livro - Class

class Restaurant ():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant (self):#lembre-se que nessa função não precisa colocar todos os parâmetros, basta o self
		print("O nome do restaurante é {} e o tipo de cuzinha é {}".format(self.restaurant_name,self.cuisine_type))

	def open_restaurant(self):#lembre-se que nessa função não precisa colocar todos os parâmetros, basta o self
		print("O restaurante {} abre às 8hs e fecha às 22hs".format(self.restaurant_name))	

rest1 = Restaurant("Bom Gosto", "popular brasileira")
rest2 = Restaurant("Mori", "japonesa")

print(rest1.describe_restaurant())
print("\n")
print(rest2.open_restaurant())

		
#criando uma classe filha (herança)

class IceCreamStand (Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)    
		#observe que a função "super()"" permite pegar os parâmetros da classe pai
		#os métodos acima tem por função vincular a class mão a class filha

		

	def describe_ice (self):
		print("Minha sorveteria se chama {}".format(self.restaurant_name))
		#esse método foi incluido para testar a vinculação entre classes
		#o método restaurant_name foi herdado da class mãe, e está sendo usado na filha


	def order_ice (self, bolas, sabor):
		self.bolas = bolas
		self.sabor = sabor
		print("meu sorvete terá {} bolas e com o seguinte sabor: {}".format(self.bolas,self.sabor))
		#esse método é restrito a class filha. Não tem relação com a class mãe

minha_sorveteria = IceCreamStand("flocos de neve","sorveteria")

print(minha_sorveteria.describe_ice())

print(minha_sorveteria.order_ice(2,"manga")) #esse método é da classe filha, e exige colocar 2 parâmentros entre parênteses