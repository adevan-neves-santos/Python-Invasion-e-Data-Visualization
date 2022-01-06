import matplotlib.pyplot as plt
import csv
from datetime import  datetime

try:
    temperaturas_max_ano=[]
    temperaturas_min_ano=[]
    datas=[]
    path_arquivo='aplicacao/segunda_fase/cap16/dados/sitka_weather_07-2018_simple.csv'
    with open(path_arquivo) as f:
        leitor=csv.reader(f)
        cabecalho=next(leitor)

        for linha in leitor:
            temperaturas_max_ano.append(int(linha[5]))
            datas.append(datetime.strptime(linha[2],'%Y-%m-%d'))
            temperaturas_min_ano.append(int(linha[6]))

    #Tenho as temperaturas máxima e suas datas
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(datas,temperaturas_max_ano,c='red')
    plt.plot(datas,temperaturas_min_ano,c='blue')
    plt.fill_between(datas,temperaturas_max_ano,temperaturas_min_ano,facecolor='blue',alpha=0.1)

    #Formatação de gráfico
    plt.title("Dias com temperaturas máximas e mínimas, julho de 2018",fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperatura (F°)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.savefig("aplicacao/segunda_fase/cap16/imagens/sitka_temp.png")
    plt.show()

except FileNotFoundError:
    print("Não encontramos o arquivo. Verifique o caminho novamente !")