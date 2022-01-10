import matplotlib.pyplot as plt

'''

15.1 – Cubos: Um número elevado à terceira potência é chamado de cubo. Faça
a plotagem dos cinco primeiros números elevados ao cubo e, em seguida, dos
primeiros 5.000 números elevados ao cubo.
15.2 – Cubos coloridos: Aplique um colormap ao seu gráfico de cubos.

'''

cinco_cubicos=list(range(1,6))
cinco_cubicos2=[x**3 for x in cinco_cubicos]

cinco_mil_cubicos=list(range(1,5001))
cinco_mil_cubicos2=[x**3 for x in cinco_mil_cubicos]

plt.scatter(cinco_cubicos,cinco_cubicos2,s=23,c=cinco_cubicos,cmap=plt.cm.Blues)
plt.title("Cinco primeiros cúbicos !", fontsize=17)
plt.xlabel("Números Naturais",fontsize=10)
plt.ylabel("Seus respectivos cúbicos",fontsize=12)
plt.savefig("Projeto-02/adevanDataVisualization/cap15Treino/imagens/cinco-primeiros-cubos.png")
plt.show()

plt.scatter(cinco_mil_cubicos,cinco_mil_cubicos2,s=1,edgecolor='none',c=cinco_mil_cubicos,cmap=plt.cm.Reds)
plt.title("Cinco mil primeiros cúbicos !", fontsize=11)
plt.xlabel("Números Naturais",fontsize=8)
plt.ylabel("Seus respectivos cúbicos",fontsize=9)
plt.savefig("Projeto-02/adevanDataVisualization/cap15Treino/imagens/OutraImagem.png")
plt.show()