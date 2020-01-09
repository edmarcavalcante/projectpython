#lista_familia = ['edmar', 'jamille', 'lúcia', 'luciana', 'priscilla', 'rômulo', 'arildo', 'jaqueline', 'andré', 'rita', 'nabor']
sobrinhos = ['júlia', 'mariana', 'gabriel', 'lara', 'luca']
irma = ['priscilla', 'luciana']
cunhado = ['rômulo', 'arildo', 'jaqueline', 'andré']
esposa = ['jamille']
mae = ['lúcia']
sogros = ['rita', 'nabor']
familia = sobrinhos + irma + cunhado + esposa + mae + sogros

for membro in familia:
	if membro in irma:
		print('olá ' + membro+', você é minha irmã'+ '\n')
	if membro in sobrinhos:
		print(membro + ', titio te ama!!'+ '\n')
	if membro in cunhado:
		print('gosto muito de você, ' + membro + '\n')
	if membro in esposa:
		print('TE AMO MUITO,'+ membro + '\n')

print('EU AMO TODOS VOCÊS!!!')


