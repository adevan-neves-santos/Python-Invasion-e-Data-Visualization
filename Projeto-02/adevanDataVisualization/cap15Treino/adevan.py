import matplotlib.pyplot as plt
import pygal
from passeio_aleatorio import Passeio_Aleatorio
from dado import Dado

#15.10 – Exercitando as duas bibliotecas: Experimente usar o matplotlib para criar
#uma visualização de lançamento de dados e use o Pygal para criar uma
#visualização de um passeio aleatório.

# Objetos utilizados nos gráficos
d1=Dado(22)
pa=Passeio_Aleatorio(1200)

resultados=[]
for i in range(100):
    resultados.append(d1.jogar())

frequencias=[]
possiveis=list(range(1,d1.numero_lados+1))
for i in range(1,d1.numero_lados+1):
    frequencias.append(resultados.count(i))

plt.figure(figsize=(10,6))
plt.plot(possiveis,frequencias,c='green')
plt.title("Frequências de lados em um dado de 22 com 100 lançamentos")
plt.xlabel("Lados",fontsize=12)
plt.ylabel("frequência de lados")
plt.savefig('Projeto-02/adevanDataVisualization/cap15Treino/imagens/dadosMatplotlib.png')
plt.show()

pa.calcular_passeio()

listaPontos=[]
for i in range(1200):
    tup=(pa.x_valores[i],pa.y_valores[i])
    listaPontos.append(tup)
tabela=pygal.XY(stroke=False)
tabela.title="Passeio Aleatório com 1200 pontos"
tabela.add("Pontos",listaPontos)
tabela.render_to_file("Projeto-02/adevanDataVisualization/cap15Treino/imagens/passeio.svg")
tabela.render()