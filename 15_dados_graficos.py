#_____GERANDO DADOS E GRÁFICOS_____

#quando se trabalha com visualização de dados/gráficos, uma das ferramentas mais importantes
# é a biblioteca matplotlib, que é uma biblioteca matemática para construção de gráficos

#Outra ferramenta interessante é o Pygal, cria visualizaçõe que funcinam bem em dispositivos digitais

#__Galeria do matplotlib = http://matplotlib.org - na galeria você pode ver os tipos de gráficos que
# a ferramenta pode criar. É possível também ver o código usado para gerar o gráfico.

# primeiro passo - importar a biblioteca matplotlib

import matplotlib.pyplot as plt 
# o módulo pyplot contém várias funções que ajudam a gerar gráficos e pltagens

meus_dados = [2,3,5,9,15]

plt.plot(meus_dados)
plt.show()

plt.plot(meus_dados, linewidth=5) # o parâmetro linewidgth controla a espessura da linha gerada por plot()

#definir o título do gráfico e nemiar os eixos

plt.title("Gráfico de Teste")
plt.ylabel("Eixo Y")
plt.xlabel("Eixo x")

plt.show()


idade = [2,8,14,19,25,30]
peso = [40,42,55,62,68,75]
plt.plot(idade,peso)
plt.ylabel("Peso do paciente")
plt.xlabel("Idade do paciente")
plt.show()

# A função scatter() plota pontos ao invés de linhas

x = [2,5,8,10,14]
y = [10,20,30,40,50]

plt.scatter(x,y, s=100) # o argumento s define o tamanho dos pontos
plt.xlabel("ponto x")
plt.ylabel("ponto y")

plt.show()

# criando um lista automática
x_valor = list(range(1,100))
y_valor = [x**1.5 for x in x_valor] # utilizamos a list comprehension para gerar os valores de y_valor
plt.plot(x_valor,y_valor)
plt.title("Gráfico valores automáticos")
plt.xlabel("valores de x")
plt.ylabel("valores de y na potência 1,5")
plt.axis([10,90,20,800]) # a função axis especifica o intervalo de cada eixo que será plotado. Ele exige 4 valores
# mín e máx do eixo x e min e máx do eixo y. O intervalo deve estar entre cochetes
plt.show()
