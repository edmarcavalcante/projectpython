minha_lista = ['itália', 'frança', 'alemanhã', 'holanda']

novo_pais = input("Qual país você desejaria conhecer? ")

if novo_pais in minha_lista:
	print('você já conhece esse país!!')
else:
	minha_lista.append(novo_pais)
	print('Ótimo, '+ novo_pais.upper() + ' é um belo país para se conhcer')

print(minha_lista)
	