from matplotlib import pyplot as plt
import csv
from datetime import datetime

death='Projeto-02/adevanDataVisualization/cap16Exercicios/datasets/death-valley-california-july-2021.csv'
san='Projeto-02/adevanDataVisualization/cap16Exercicios/datasets/san-franciso-california-july-2021.csv'
sit='Projeto-02/adevanDataVisualization/cap16Exercicios/datasets/sitka-alasca-july-2021.csv'

### Comparar San Francisco com Sitka e Death Valley

max_death=[]
min_death=[]
date_death=[]

max_san=[]
min_san=[]
date_san=[]

max_sit=[]
min_sit=[]
date_sit=[]

with open(death) as f:
    leitor=csv.reader(f)
    cabecalhos=next(leitor)
    
    for linha in leitor:
        try:
            max_death.append(int(linha[1]))
            min_death.append(int(linha[2]))
            date_death.append(datetime.strptime(linha[0],'%Y-%m-%d'))
        except ValueError:
            print("Erro de campo na data "+linha[0])

with open(san) as f:
    leitor=csv.reader(f)
    cabecalhos=next(leitor)
    
    for linha in leitor:
        try:
            max_san.append(int(linha[1]))
            min_san.append(int(linha[2]))
            date_san.append(datetime.strptime(linha[0],'%Y-%m-%d'))
        except ValueError:
            print("Erro de campo na data "+linha[0])

with open(sit) as f:
    leitor=csv.reader(f)
    cabecalhos=next(leitor)
    
    for linha in leitor:
        try:
            max_sit.append(int(linha[1]))
            min_sit.append(int(linha[2]))
            date_sit.append(datetime.strptime(linha[0],'%Y-%m-%d'))
        except ValueError:
            print("Erro de campo na data "+linha[0])

#Agora disposto das informações podemos plotar os gráficos de temperatura para análise.



fig_death=plt.figure(dpi=118,figsize=(9,5))

plt.plot(date_death,max_death,c='red')
plt.plot(date_death,min_death,c='blue')
plt.title("Variação de Temperatura no Death Valley em julho de 2021",fontsize=19)
plt.ylabel("Temperatura (F)",fontsize=12)
plt.xlabel("",fontsize=12)
fig_death.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=12)
plt.fill_between(date_death,max_death,min_death,facecolor='green',alpha=0.2)
plt.savefig('Projeto-02/adevanDataVisualization/cap16Exercicios/imagens/death-valley.png')
plt.show()



fig_san=plt.figure(dpi=118,figsize=(9,5))

plt.plot(date_san,max_san,c='red')
plt.plot(date_san,min_san,c='blue')
plt.title("Variação de Temperatura em San Francisco no mês julho de 2021",fontsize=19)
plt.ylabel("Temperatura (F)",fontsize=12)
plt.xlabel("",fontsize=12)
fig_san.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=12)
plt.fill_between(date_san,max_san,min_san,facecolor='green',alpha=0.2)
plt.savefig('Projeto-02/adevanDataVisualization/cap16Exercicios/imagens/san-fracisco.png')
plt.show()

fig_sit=plt.figure(dpi=118,figsize=(9,5))

plt.plot(date_sit,max_sit,c='red')
plt.plot(date_sit,min_sit,c='blue')
plt.title("Variação de Temperatura em Sitka no mês julho de 2021",fontsize=19)
plt.ylabel("Temperatura (F)",fontsize=12)
plt.xlabel("",fontsize=12)
fig_sit.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=12)
plt.fill_between(date_sit,max_sit,min_sit,facecolor='green',alpha=0.2)
plt.savefig('Projeto-02/adevanDataVisualization/cap16Exercicios/imagens/sitka.png')
plt.show()