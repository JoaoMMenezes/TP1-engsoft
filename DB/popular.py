import pandas as pd
from random import randint, choice, seed
import names
import sys
sys.path.insert(0, r'.\TP1-engsoft\Backend\ru-server\utils')
from dbframe import  df2SQL, connect
import numpy as np

seed(10)
def matricula_generator(size):
     dados = list()
     for x in range(0,size):
          dados.append( randint(1000000000, 9999999999) )

     return dados

def nome_generator(size):
     dados = list()
     for x in range(0,size):
          dados.append( names.get_full_name() )
     return dados

def senha(size):
     dados = list()
     for x in range(0,size):
          dados.append( randint(100, 100000) )
     return dados

def ficha(size):
     dados = list()
     for x in range(0,size):
          dados.append( randint(0, 50) )
     return dados

def tipo(size):
     tipos = [0, 1, 2.9, 5.6, 6, 8.5]
     dados = list()
     for x in range(0,size):
          dados.append( choice(tipos) )
     return dados

def email(size):
     dados = list()
     for x in range(0,size):
          dados.append(None)
     return dados


def clientes(inicio, fim, frequencia = "T"):
     datas = pd.date_range(start= inicio, end=fim, periods= 950).strftime('%Y%m%d %H:%M:%S').tolist()
     tamanho = len(datas)
     print(tamanho)
     matriculas = matricula_generator(tamanho)
     comando = "insert [dbo].[Clientes] values "
     for index, valores in enumerate(zip(matriculas, datas) ):
          if(index != tamanho-1):
               aux_str = "("+ str(valores[0])+ ",\'"+ str(valores[1])+  "\'),"
          else:
               aux_str = "("+ str(valores[0])+ ",\'"+ str(valores[1])+ "\')"
          comando = comando + aux_str
     print(comando)
     inserir = pd.DataFrame({"Matricula": matriculas, 
                        "Senha": senha(tamanho),
                          "Nome": nome_generator(tamanho),
                          "Fichas": ficha(tamanho) ,
                          "ValorFicha": tipo(tamanho),
                          "Email" : email(tamanho)
                          })
     df2SQL(inserir," dbo.Usuario0", connect("LAPTOP-4BELV735", "credito_ru"))


clientes('2023-04-14 10:50:00', '2023-04-15 14:30:00') 
 #pegar o comando e jgoar no sql server 
#df2SQL(tes, "[dbo].[Clientes]", conexao)



