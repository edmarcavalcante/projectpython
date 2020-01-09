#Programa de Pizzaria

print("SEJA BEM VIDO A PIZZARIA DO ED!\nESCOLHA O TAMANHO:\n\n[1]Pequena\n[2]Média\n[3]Grande")

tamanho_escolhido = int(input('\nQual o tamanho de sua Pizza? '))

if tamanho_escolhido == 1:
	print('\nVocê escolheu a pizza pequena, logo poderá escolher 2 sabores')
if tamanho_escolhido == 2:
	print('\nVocê escolheu a pizza média, logo poderá escolher 4 sabores')
if tamanho_escolhido == 3:
	print('\nVocê escolheu a pizza grande, logo poderá escolher 6 sabores')

sabores_disponíveis = ['calabresa', 'frango', 'palmito', 'carne do sol', 'quatro queijos', 'atum', 'marguerita']

print('\nNO MOMENTO NOSSA PIZZARIA DISPÕE DOS SEGUINTES SABORES:\n')
for sabor in sabores_disponíveis: 
	print(sabor.upper())

if tamanho_escolhido == 1:
	sabor_1 = input('Escolha seu primeiro sabor: ')
	if sabor_1 in sabores_disponíveis:
		print('Escolha o próximo')
	else:
		print('Não temos esse sabor no momento, desculpe.')
	sabor_2 = input('Escolha seu segundo sabor: ')
	if sabor_2 in sabores_disponíveis:
		print('Obrigado, sua pizza terá os seguintes sabores: ' + sabor_1 + ' e ' + sabor_2)
	else:
		print('Não temos esse sabor no momento, desculpe. Escolha novamente.')
		sabor_2 = input('Escolha seu segundo sabor: ')
#como eu faço para que toda vez que o cliente escolha um sabor inexistente ele volte automaticamente a situação de escolha?

3004-8007





