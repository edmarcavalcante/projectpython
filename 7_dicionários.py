# TRABALHANDO COM DICIONÁRIOS EM PYTHON
registro_amigos = {"nome": "Juca","idade": 33, "peso": 83,}

print(registro_amigos)

print(registro_amigos['nome']) # informa o valor contido na chave 'nome'
print(registro_amigos['idade'])
print(registro_amigos['peso'])


#percorrer todos os pares chave-valor com um laço

for key, value in registro_amigos.items():
	print("\nKey: " + key)
	print("\nvalue " + str(value))

print("\n\n")

favorite_languages = {
	'Edmar': 'python',
	'Fábio': 'java',
	'raimundo': 'C++',
	'Antônio': 'SQL',
	}

for nome, language in favorite_languages.items():
	if language != 'SQL':
		print(language.title() + ' is the favorite language of the ' + nome.title())
	else:
		print(language.upper() + ' is the favorite language of the ' + nome.title())

print("\n\n")
#esse if-else foi apenas para ajustar o nome SQL, deixando ele em letras maículas

# se eu qusiser buscar através dos lanço somente o valor da chave, posso fazer da seguinte forma:
corregedoria = ["Fábio", "Antônio"]
for key in favorite_languages.keys():
	print(key.title())
	if key in corregedoria:
		print("hello " + key + ", you used the language " + favorite_languages[key])
# o python vai pegar percorrer todas as chaves e salvar na variável 'nome'. Em seguida, irá 
# informar uma por uma.

print("\n\n")



user_1 = {"nome": "luciana", "idade": 37, "cor": "branca", "parentesco": "irmã"}
user_2 = {"nome": "priscilla", "idade": 35, "cor": "morena", "parentesco": "irmã"}
user_3 = {"nome": "jamille", "idade": 31, "cor": "morena", "parentesco": "esposa"}

familia = [user_1, user_2, user_3]

for membro in familia:
	if membro["nome"] == "jamille":
		print(membro["nome"] + " é minha esposa")
	else:
		print(membro["nome"] + " é minha irmã")	
# acima, fiz um loop que percorreu um dicionário que está dentro de uma lista.

print("\n")

for membro in familia:
	for key, value in membro.items():
		if value == 31:
			print(key + "é minha esposa")
		if value == 35:
			print(key + " é minha irmã do meio, e tem duas filhas: júlia e mari")
		if value == 37:
			print(key + " é minha irmã mais velha, e tem um filho chamado luca")
print("\n")

print("CONCLUÍMOS O CAPÍTULO DE DICIONÁRIOS E LISTAS")
