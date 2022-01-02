import pygal
from dado import Dado

d1=Dado()
d2=Dado()
resultados=[]

for i in range(1000):
    resultados.append(d1.jogar()+d2.jogar())

resultado_maximo=d1.numero_lados+d2.numero_lados
frequencias=[]
for i in range(2,resultado_maximo+1):
    frequencia=resultados.count(i)
    frequencias.append(frequencia)

hist=pygal.Bar()
hist.title="Resultado de 1000 lançamentos de dois dados simultâneos"
hist.x_labels=['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="Resultados"
hist.y_title="Frequência de resultado"
hist.add("D6+D6",frequencias)

hist.render_to_file("aplicacao/lancamento-de-dados/visualizacaoDoisDados.svg")