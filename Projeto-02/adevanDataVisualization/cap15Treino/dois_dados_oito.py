from dado import Dado
import pygal

d1=Dado(8)
d2=Dado(8)
d3=Dado(8)

resultados=[]
for i in range(50000):
    resultados.append(d1.jogar()+d2.jogar()+d3.jogar())

frequencias=[]
resultado_maximo=d1.numero_lados+d2.numero_lados+d3.numero_lados
for i in range(3,resultado_maximo+1):
    freq=resultados.count(i)
    frequencias.append(freq)

fig=pygal.Bar()
fig.title="50000 Lançamentos de três dados com 8 lados ."
fig.x_labels=[str(elem) for elem in (list(range(2,d1.numero_lados*3+1)))]
fig.x_title="Resultados"
fig.y_title="Frequência de resultados"
fig.add("D8+D8",frequencias)
fig.render_to_file("Projeto-02/adevanDataVisualization/cap15Treino/imagens/OitoLadosTresDados.svg")