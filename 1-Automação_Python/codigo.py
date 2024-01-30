#Código para resolver este projeto de automação na Jornada Python da Hashtag Programação
#-----------------------------------------/--------------------------------------------

#---Importações de bibliotecas a serem utilizadas para o projeto
#"Pyautogui" para automação, "time" para pequenas pausas no código e "pandas" para poder importar o arquivo csv desejado

import pyautogui as pg
import time
import pandas as pd

#---Importando a tabela 'produtos'
def importacaoCsv():
    tabela = pd.read_csv('D:\Jornada-Python_HASHTAG\PythonPowerUP\produtos.csv')
    print(tabela)
    return tabela
tabela = importacaoCsv()

pg.PAUSE=0.5

#---Passo inicial para abrir o navegador
def EntradaNavegador():
    pg.press('win')
    pg.write('Chrome')
    pg.press('Enter')
    return
EntradaNavegador()

#---Entrando no site 
def Sistema():
    link= 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    pg.write(link)
    pg.press('Enter')
    
    #Fazendo login
    #Email 
    pg.sleep(1)
    pg.click(x=810, y=374)
    pg.write('marcos_python@projeto.com')
    pg.press('tab')
    #Senha
    pg.write('datascience')
    pg.press('Enter')
    
    return
Sistema()

#---Cadastro de produtos
for linha in tabela.index:
       
    try:
        pg.click(x=757, y=257)
        pg.sleep(2)
    except Exception as e:
        print(f"Erro durante o cadastro do produto na linha {linha}: {e}")

    # Codigo 
    codigo = tabela.loc[linha, 'codigo']
    pg.write(codigo)
    pg.press('tab')
    pg.sleep(1)

    # Marca
    marca = tabela.loc[linha, 'marca']
    pg.write(marca)
    pg.press('tab')

    # Tipo
    tipo = tabela.loc[linha, 'tipo']
    pg.write(tipo)
    pg.press('tab')

    # Categoria
    categoriaProduto = str(tabela.loc[linha, 'categoria'])
    pg.write(categoriaProduto)
    pg.press('tab')

    # Preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pg.write(preco)
    pg.press('tab')

    # Custo Unitário
    custoProduto = str(tabela.loc[linha, 'custo'])
    pg.write(custoProduto)
    pg.press('tab')

    # Observações
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pg.write(str(obs))
    pg.press('tab')
    pg.press('enter')