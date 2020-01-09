# APRENDENDO A USAR LIST COMPREHENSIONS
# a list comprehensions permite desenvolver uma lista usando uma notação diferente.
# seria essencialmente um loop for dentro de []

# ex:      lst=[x for x "sequência"]

# a estrutura de list comprehensions apresenta desempenho muito supeiror do que as outras 
# estruturas
# é muito mais veloz do que a função MEP
# quando se estiver diante de um grande volume de dados, vale a pena usá-la
# verificar se é possível aplicar a list comprehensions


list_a = [x for x in "Edmar"]
# a leitura que se faz dessa notação é: eu vou retornar x para cada x que tiver na string.
print(list_a)

# outro exemplo

print("\n")

lista_b = [x**2 for x in range(0,9)]
print(lista_b)

#exemplo da trasnfornação de graus celsius para fahrenheit

celsius = [10, 15, 20, 25, 30]

fahrenheit = [(c*1.8)+32 for c in celsius]
print(fahrenheit)
# essa função traz o mesmo resultado que a função MAP, só que com muito menos código, o que a torna mais veloz.