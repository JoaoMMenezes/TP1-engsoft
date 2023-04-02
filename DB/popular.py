import pandas as pd
import utils
from random import randint
import names

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



teste = nome_generator(10)
print(teste)