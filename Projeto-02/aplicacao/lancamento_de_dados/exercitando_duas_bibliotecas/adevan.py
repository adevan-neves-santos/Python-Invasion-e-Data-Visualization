import matplotlib.pyplot as plt
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
for i in range(1,d1.numero_lados+1):
    f=resultados.count(i)
    frequencias.append(f)

ladosPossiveis=list(set(resultados)).sort()
print(len(ladosPossiveis))
print(len(frequencias))
