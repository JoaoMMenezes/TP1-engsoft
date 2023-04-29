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
def get_columns_name(table, connection, option = 1):
    """
    Esta função retorna o nome das culunas de uma tabela
    
    Parameters
    ----------
        table_name (str): name of the table  EX -> Table_1
        connection (str): connection point use connect() function
        option (int): 1 retorna um dataframe e 0 retorna uma lista
    """
    command = 'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME =\'' + table +'\''
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
            conn.execute("insert "+p_table_name+ " values("+inter[:-1]+")", row)
##########################################################################################################
def insert_1_element(data, table_name, connection):
    """
    Esta função retorna o ultimo id(chave) da tabela
    
    Parameters
    ----------
        data (list): a list with all values EX -> ["nome", 65, 1.1, ultimo+1, None]
        p_table_name (str): path of table EX -> dbo.Table_1
        connection (str): connection point use connect() function
    """
    inter = "?,"*len(data)
    command = "insert "+table_name+ " values("+inter[:-1]+")"
    with connection.begin() as conn:
        conn.execute(command,data)
##########################################################################################################

def update_1_element(table_name, connection, coluna, valor, coluna2, valor2):
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
    command = "update " + table_name+ " set "+ str(coluna) +" = "+ str(valor) + " where " + str(coluna2) +" = " + str(valor2) 
    with connection.begin() as conn:
        conn.execute(command)

################################
# RELATIONAL ALGEBRA FUNCTIONS #
################################

def SQL_SELECT(table, condition, connection, option = 1):
    """
    Função para o operador de seleção (SELECT)
    
    Parameters
    ----------
        table (str): the name of the wanted table to be worked on, e.g. ("EMPLOYEE")
        condition (str): the condition which must be satisfied in query language, e.g. ("Dno = 5 AND Salary > 25000")
        connection (str): connection point use connect() function
        option (int): 1 retorna um dataframe e 0 retorna uma lista
    """
    command = 'SELECT * FROM ' + table + ' WHERE ' + condition +';'
    with connection.begin() as conn:
        if option:
            outpout = pd.read_sql_query(sa.text(command), conn)
        else:
           outpout = conn.execute(sa.text(command)).fetchall()
    return outpout
##########################################################################################################
def SQL_PROJECT(table, column_name, connection, case = "DISTINCT", option = 1):
    """
    Função para o operador de projeção (PROJECT)
    
    Parameters
    ----------
        table (str): the name of the wanted table to be worked on, e.g. ("EMPLOYEE")
        column_name (str): column names in which you want the projection, e.g. ("Sex, Salary")
        case (str): DISTINCT must be defined if duplicateds are NOT WANTED, otherwise ' ' must be set, e.g. ('') or let default
        connection (str): connection point use connect() function
        option (int): 1 retorna um dataframe e 0 retorna uma lista
    """
    command = 'SELECT ' + case + ' ' + column_name + ' FROM ' + table +';'
    with connection.begin() as conn:
        if option:
            outpout = pd.read_sql_query(sa.text(command), conn)
        else:
           outpout = conn.execute(sa.text(command)).fetchall()
    return outpout
##########################################################################################################
def SQL_RENAME(table, new_table_name, actual_column_names, new_column_names, connection, option = 1):
    """
    Função para o operador de renomeação (RENAME)
    
    Parameters
    ----------
        table (str): the name of the wanted table to be worked on, e.g. ("EMPLOYEE")
        new_table_name (str) (array): default is set to '' since it is optional since the primarly objective is change the column names
        actual_column_names (str) (array): the columns names from the table which are supposed to be changed
        new_column_names (str): the new column names that must be set in the order to match its respective actual_column_name
        connection (str): connection point use connect() function
        option (int): 1 retorna um dataframe e 0 retorna uma lista
    """
    aux_command = []
    for x in range(len(actual_column_names)):
        aux_command.append(actual_column_names[x] + ' AS ' + new_column_names[x] + ', ')

    aux_command = ''.join(aux_command)
    aux_command = aux_command[:-2]
    if len(new_table_name) == 0:
        command = 'SELECT ' + aux_command + ' FROM ' + table +';'
    else:
        command = 'SELECT ' + aux_command + ' FROM ' + table + ' AS ' + new_table_name +';'
  
    with connection.begin() as conn:
        if option:
            outpout = pd.read_sql_query(sa.text(command), conn)
        else:
           outpout = conn.execute(sa.text(command)).fetchall()
    return outpout
##########################################################################################################
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

