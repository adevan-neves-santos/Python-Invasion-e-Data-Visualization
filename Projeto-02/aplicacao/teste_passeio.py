from passeio_aleatorio import Passeio_Aleatorio
import matplotlib.pyplot as plt
import os

pa=Passeio_Aleatorio()
pa.calcular_passeio()
intervalo=list(range(pa.numero_pontos))
plt.scatter(pa.x_valores,pa.y_valores,c='red',s=7,edgecolor='none')

plt.title("Passeio Aleatório com 5000 pontos !",fontsize=12)
if(os.path.exists("aplicacao/imagensPasseio/Passeio.png")):
    os.remove("aplicacao/imagensPasseio/Passeio.png")
plt.savefig("aplicacao/imagensPasseio/Passeio.png",bbox_inches="tight")
plt.show()

#Usando colormap
plt.scatter(pa.x_valores,pa.y_valores,c=intervalo,cmap=plt.cm.Blues,s=7,edgecolor='none')
plt.scatter(0,0,c='green',s=23,edgecolor='none')
plt.scatter(pa.x_valores[-1],pa.y_valores[-1],c='red',s=23,edgecolor='none')
plt.title("Passeio Aleatório com 5000 pontos e colorMap !",fontsize=12)
plt.savefig("aplicacao/imagensPasseio/PasseioColorMap.png",bbox_inches="tight")
plt.show()

print("Fim !")
