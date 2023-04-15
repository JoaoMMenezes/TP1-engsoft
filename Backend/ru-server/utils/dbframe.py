from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import sqlalchemy as sa
import pandas as pd

def connect(servidor, banco_de_dados, driver = "ODBC Driver 17 for SQL Server"):
    """
    Esta função irá retornar o ponto de conexão
    
    Parameters
    ----------
        servidor (str): use "SELECT @@SERVERNAME" no SQL server management para descobrir
        banco_da_dados (str): string do nome do banco
        driver (str): use driver_name = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')][0]
    """
    connection_string = "DRIVER={"+driver+"};SERVER="+servidor+";DATABASE="+banco_de_dados+ ";trusted_connection=yes;"
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)
    return engine
##########################################################################################################

def SQL2df(command, connection, option = 1):
    """
    Esta função generica para acesar e pegar qualquer dado de uma tabela
    
    Parameters
    ----------
        command (str): SQL query
        connection (str): connection point use connect() function
        option (int): 1 retorna um dataframe e 0 retorna uma lista
    """
    with connection.begin() as conn:
        if option:
            outpout = pd.read_sql_query(sa.text(command), conn)
        else:
           outpout = conn.execute(sa.text(command)).fetchall()
    return outpout
##########################################################################################################
def get_columns_name(table_name, connection, option = 1):
    """
    Esta função retorna o nome das culunas de uma tabela
    
    Parameters
    ----------
        table_name (str): name of the table  EX -> Table_1
        connection (str): connection point use connect() function
        option (int): 1 retorna um dataframe e 0 retorna uma lista
    """
    command = 'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME =\'' + table_name +'\''
    with connection.begin() as conn:
        if option:
            outpout = pd.read_sql_query(sa.text(command), conn)
        else:
           outpout = conn.execute(sa.text(command)).fetchall()
    return outpout
##########################################################################################################
def df2SQL(df, p_table_name, connection):
    """
    Esta função passa um dataframe para a base SQL
    
    Parameters
    ----------
        df (dataframe): a dataframe with columns name
        p_table_name (str): path of table EX -> [dbo].[Table_1]
        connection (str): connection point use connect() function
    """
    col = len(df.columns )
    inter = "?,"*col
    with connection.begin() as conn:
        for index, row in df.iterrows():
            conn.execute("insert"+p_table_name+ " values("+inter[:-1]+")", row)
##########################################################################################################
def get_last_id(p_table_name, connection):
    """
    Esta função retorna o ultimo id(chave) da tabela
    
    Parameters
    ----------
        p_table_name (str): path of table EX -> dbo.Table_1
        connection (str): connection point use connect() function
    """
    command = "SELECT id FROM "+p_table_name +" WHERE id = (SELECT MAX(id) FROM "+p_table_name+ " )"
    with connection.begin() as conn:
          return conn.execute(sa.text(command)).fetchall()[0][0]
##########################################################################################################
def insert_1_element(data, p_table_name, connection):
    """
    Esta função retorna o ultimo id(chave) da tabela
    
    Parameters
    ----------
        data (list): a list with all values EX -> ["nome", 65, 1.1, ultimo+1, None]
        p_table_name (str): path of table EX -> dbo.Table_1
        connection (str): connection point use connect() function
    """
    inter = "?,"*len(data)
    command = "insert "+p_table_name+ " values("+inter[:-1]+")"
    with connection.begin() as conn:
        conn.execute(command,data)
##########################################################################################################

def update_1_element(p_table_name, connection, coluna, valor, coluna2, valor2):
    """
   Esta função atualiza o valor de um elemento da tabela
    
    Parameters
    ----------
        p_table_name (str): path of table EX -> dbo.Table_1
        connection (str): connection point use connect() function
        coluna (str): coluna to set the value EX -> "Fichas"
        valor (str): new value to set Ex -> "8"
        coluna2 (str): coluna to refer the value to set EX -> "Matricula"
        valor2 (str): value in coluna to refer the value to set Ex -> "10000000"
        
    """
    command = "update " + p_table_name+ " set "+ str(coluna) +" = "+ str(valor) + " where " + str(coluna2) +" = " + str(valor2) 
    with connection.begin() as conn:
        conn.execute(command)


"""
servidor = "LAPTOP-4BELV735"
banco_de_dados = "teste"
e = connect(servidor,banco_de_dados)
df = SQL2df("SELECT * FROM dbo.Table_1 ", e, 0)
print(df)
colunas = get_columns_name("Table_1", e, 1)
print(colunas.values[0][0])
ultimo = get_last_id("dbo.Table_1", e)
print(ultimo)

inserir = pd.DataFrame({"nome": ["fffff", "gggggggggg"], 
                        "idade": [45,35],
                          "dinheiro": [26.7, 31.8],
                          "id": [ultimo+1, ultimo+2] ,
                          "data": [None, " "]})

df2SQL(inserir,"[dbo].[Table_1]", e)
dados = e.execute("SELECT * FROM dbo.Table_1 where id = 1 ").fetchall()
print(dados)



d = {"nome": "aba","idade": 55,"dinheiro": 31,  "id": ultimo+1 , "data": None}
d = ["llll", 65, 1.1, ultimo+1, None]
#insert_1_element(d, "dbo.Table_1", e)
"""

