#------------------------------------------------------------------------------
#Código de auxílio para capturar coordernadas na tela e poder fazer automações
 #Importação das bibliotecas pyautogui e time
import pyautogui as pg
import time 

#Atraso de 5 segundos para poder capturar coordernadas desejadas no site
time.sleep(5)
#Mostrar a coordernada obtida
print(pg.position()) 