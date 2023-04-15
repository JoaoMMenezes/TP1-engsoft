import pandas as pd
import sys
sys.path.insert(0, r'.\TP1-engsoft\Backend\ru-server\utils')
from dbframe import SQL2df, connect
import dbacess
from datetime import datetime 


conexao = dbacess.ServerAcess("LAPTOP-4BELV735", "credito_ru")
#definir datas de começo e final 
data_i = datetime(2023, 4, 14, 00, 00, 59)
data_fim = datetime(2023,4,15, 23,55,59)
print(data_i)
#pegar dados dos clientes
dados = SQL2df("select * from dbo.Clientes", conexao.connection)
print(dados.head())
print(dados.shape)

#pegar dados do usario
user = SQL2df("select Matricula, ValorFicha from dbo.Usuario0", conexao.connection)
print(user.head())
print(user.shape)

final = pd.merge(dados, user, how="outer")
print(final.head)
