### Comparar Sitka (Alasca) com Death Valley (Las Vegas) de maneira apropriada
from datetime import datetime
import csv
from matplotlib import pyplot as plt


local='Projeto-02/adevanDataVisualization/cap16Exercicios/datasets/'
local_imagens='Projeto-02/adevanDataVisualization/cap16Exercicios/imagens/'
nome_death='death-valley-california-july-2021.csv'
nome_sitka='sitka-alasca-july-2021.csv'
path_death=local+nome_death
path_sitka=local+nome_sitka

max_death=[]
min_death=[]
date_death=[]

max_sit=[]
min_sit=[]
date_sit=[]

with open(path_death) as f:
    leitor=csv.reader(f)
    cabecalhos=next(leitor)
    
    for linha in leitor:
        try:
            max_death.append(int(linha[1]))
            min_death.append(int(linha[2]))
            date_death.append(datetime.strptime(linha[0],'%Y-%m-%d'))
        except ValueError:
            print("Erro de campo na data "+linha[0])

with open(path_sitka) as f:
    leitor=csv.reader(f)
    cabecalhos=next(leitor)
    
    for linha in leitor:
        try:
            max_sit.append(int(linha[1]))
            min_sit.append(int(linha[2]))
            date_sit.append(datetime.strptime(linha[0],'%Y-%m-%d'))
        except ValueError:
            print("Erro de campo na data "+linha[0])

fig_san=plt.figure(dpi=118,figsize=(9,5))
plt.plot(date_sit,max_sit,c='red')
plt.plot(date_sit,min_sit,c='blue')
plt.axis((date_sit[0],date_sit[-1],0,120))
plt.title("Variação de Temperatura em San Francisco no mês julho de 2021",fontsize=19)
plt.ylabel("Temperatura (F)",fontsize=12)
plt.xlabel("",fontsize=12)
fig_san.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=12)
plt.fill_between(date_sit,max_sit,min_sit,facecolor='green',alpha=0.2)
plt.savefig(local_imagens+'san-fracisco2.png')
plt.show()

fig_death=plt.figure(dpi=100,figsize=(10,7))
plt.plot(date_death,max_death,c='red')
plt.plot(date_death,min_death,c='blue')
plt.axis((date_sit[0],date_sit[-1],0,120))
plt.title("Variação de Temperatura em Death Valley no mês julho de 2021",fontsize=16)
plt.ylabel("Temperatura (F)",fontsize=12)
plt.xlabel("",fontsize=12)
fig_san.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=12)
plt.fill_between(date_death,max_death,min_death,facecolor='green',alpha=0.2)
plt.savefig(local_imagens+'death-valley2.png')
plt.show()

### Tentar plotar as informações dos dois locais em um  gráfico

fig_max=plt.figure(dpi=100,figsize=(10,7))
plt.plot(date_death,max_death,c='red',linewidth=5,label="deat valley")
plt.plot(date_sit,max_sit,c='green',linewidth=5,label='sitka')
plt.legend()
plt.title("MÁXIMAS Temperaturas registradas em Sitka e Death Valley no mes de julho em 2021.",fontsize=19)
plt.ylabel("Temperatura (F)",fontsize=12)
plt.xlabel("",fontsize=12)
fig_max.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=12)
plt.fill_between(date_death,max_death,max_sit,alpha=0.1,facecolor='green')
plt.savefig(local_imagens+'death-sitka-max-temperature.png')
plt.show()

fig_min=plt.figure(dpi=97,figsize=(10,6))
plt.plot(date_death,min_death,c='blue',linewidth=5,label="death valley")
plt.plot(date_sit,min_sit,c='green',linewidth=5,label="sitka")
plt.legend()
plt.title("Mínima Temperaturas registradas em Sitka e Death Valley no mes de julho em 2021.",fontsize=16)
plt.ylabel("Temperatura (F)",fontsize=12)
plt.xlabel("",fontsize=12)
fig_min.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=12)
plt.fill_between(date_death,min_death,min_sit,alpha=0.1,facecolor='green')
plt.savefig(local_imagens+'death-sitka-min-temperature.png')
plt.show()