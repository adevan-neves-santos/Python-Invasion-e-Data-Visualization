import json
import os

def gravar_dados():
    ## Quero gravar a string do nome do personagem, nome do jogador, quero gravar a cor de fundo
    arquivo=os.path.join("adevanAlienInvasion","config","arquivo.json")
    with open(arquivo, 'w') as fl:
        nome_jogador=input("Qual o nome do jogador ? ")
        nome_personagem=input("Qual o nome do personagem ? ")
        cor_fundo=input("Qual a cor de fundo ? ")
        json.dump(
            {'nomeJogador':nome_jogador
            ,'nomePersonagem':nome_personagem
            ,'corFundo':cor_fundo
            },
            fl,
            indent=2)
def ler_dados():
    ## Ler os dados que eu preciso
    dicionario=dict()
    arquivo=os.path.join("adevanAlienInvasion","config","arquivo.json")
    try:
        with open(arquivo,'r') as fl:
            dicionario=json.load(fl)
        return dicionario
    except FileNotFoundError:
        print("Não foi possível localizar o arquivo !!!")
    
