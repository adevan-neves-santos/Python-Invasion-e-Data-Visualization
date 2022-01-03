from passeio_aleatorio import Passeio_Aleatorio
import matplotlib.pyplot as plt
import os
'''

15.3 – Movimento molecular: Modifique rw_visual.py substituindo plt.scatter()
por plt.plot(). Para simular o percurso de um grão de pólen na superfície de
uma gota d’água, passe rw.x_values e rw.y_values e inclua um argumento
linewidth. Utilize 5.000 em vez de 50.000 pontos.

15.4 – Passeios aleatórios modificados: Na classe RandomWalk, x_step e y_step
são gerados a partir do mesmo conjunto de condições. A direção é escolhida
aleatoriamente a partir da lista [1, -1], e a distância, a partir da lista [0, 1, 2, 3,4].
Modifique os valores dessas listas para ver o que acontece com o formato geral
de seus passeios. Experimente usar uma lista maior de opções para a distância, por
exemplo, de 0 a 8, ou remova o -1 da lista de direção x ou y.

15.5 – Refatoração: O método fill_walk() é longo. Crie um novo método
chamado get_step() para determinar a direção e a distância de cada passo, e
depois calcule o passo. Você deverá ter duas chamadas para get_step() em
fill_walk():

x_step = get_step()
y_step = get_step()

Essa refatoração deverá reduzir o tamanho de fill_walk() e deixar o método
mais fácil de ler e de entender.

'''

pa=Passeio_Aleatorio(5000)
pa.calcular_passeio()
plt.plot(pa.x_valores,pa.y_valores,linewidth=1)
plt.title("Percurso de um grão de polén ")
plt.xlabel("Eixo horizontal ")
plt.ylabel("Eixo vertical ")
plt.savefig("aplicacao/passeio-exercicios/imagens/Polen.png")
plt.show()

# Modificando a lista de passos em Passeio Aleatório
