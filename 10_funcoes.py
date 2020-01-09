# ESTUDO DAS FUNÇÕES

# exemplo de primeira função
print("Bem vindo ao estudo de funções!!")



def saudacoes (username):
	'''esse comentário entre aspas tríplas é a documentação da função, descreve o que a função faz (docstring).'''
	print("Olá, "+ username.title() + "!! Seja bem vindo ao estudo de funções")

print(saudacoes("edmar"))

#atenção aos conceitos. São partes da função: parâmetro e argumento. No exemplo acima, o parâmetro é username
# o argumento é o valor que eu coloco no parâmetro, que neste caso foi edmar.

