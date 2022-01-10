from dado import Dado
import pygal
resultados=list()
dado=Dado()
for i in range(1000):
    resultados.append(dado.jogar())
print(resultados)

frequencias=[]
for i in range(1,dado.numero_lados+1):
    frequencia=resultados.count(i)
    frequencias.append(frequencia)
print(frequencias)

hist=pygal.Bar()
hist.title="Resultados para 1000 lançamentos de um dado de seis lados."
#Usar list com list comprehensions,
#hist.x_labels=['1','2','3','4','5','6']
hist.x_labels=[str(elem) for elem in (list(range(1,7)))]
hist.x_title='Resultado'
hist.y_title="Frequência de resultado"
hist.add("D6",frequencias)
hist.render_to_file("Projeto-02/adevanDataVisualization/cap15Treino/imagens/visualizacaoDados.svg")